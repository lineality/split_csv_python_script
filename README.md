# Online_Voting_Using_One_Time_Pads
Online Voting Using One Time Pads 

# Contents:
## Part 1: Secure Online Voting in Principle
## Part 2: Practical Secure Online Voting
## Part 3: Overall Voting Systems

# Clarifying Goals and Questions: 
- Main Goal: Systematize secure online voting.
- Main Questions: 
#### 1. Is secure-auditable online voting possible in principle?
#### 2. Is reliable online-vote-result-publishing possible in principle?
#### 3. Can election-processes and election-results-publishing be feasibly, sustainably, pragmatically, realistically, implemented given real world limitations on resources? 
#### 4. What are differences between ideal-maximum-security-systems and sufficiently-secure more-accessible or realistically-feasible systems?


To clarify goals and questions, below are two lists of questions. There is one list of questions that we are attempting to answer with this project, and there is another list of questions that we are NOT attempting to answer or resolve with this project. This clarification should help so that questions we are not asking do not get mixed together with questions that we are asking.


## Questions we are focusing on include the following: 
1. Is secure over-a-network (online) voting possible? (Here 'secure' is defined as being 'as secure as a non-networked paper system.') 
2. Is it possible for a voter to securely receive a ballot from a Vote-Office over a network (online)? 
3. Is it possible for a voter to submit a ballot securely over a network (online)?
4. Is it possible for a voting-office to securely receive a completed ballot from the voter over a network (online)? [including: verifying what ballot was used, verifying who submitted the ballot, checking for over errors in filling out the ballot]

## Questions that are NOT the focus of this project include the following: 
1. NOT: Can online voting be an absolutely effortless and perfectly ecstatic experience?
2. NOT: Can a person outside of the direct-voting-process be provably safe from any voter intimidation, coercion, brainwashing, threats, harassment, discouragement, etc? 
3. NOT: Can a person make no mistakes while filling out their ballot? (Though some additional safeguards from this have been successfully used in some states.) 
4. NOT: Can the physical offices of staff be absolutely impenetrable to a physical breakin or loss of records due to causes such as fires. 
5. NOT: Can hecklers and trolls be prevented from criticizing, slandering, and defaming, the election and election process even when or where there is nothing legitimate to criticize?
6. NOT: Can all disinformation campaigns be eliminated/precluded/etc.?

## A debatably separate or peripherally related question may be:
1. Are there elements of the voting process that affect (encourage or discourage) participation in the voting process (from user interface to requirements for participation to schedules of voting)? An aspect or implication of this may be inadvertent or targeted discrimination against people for whom a given system of voting is more difficult or less likely to be used.

# Concept: Universal Voting Procedures and Processes

The view taken here is that 'voting' is a science-like process. Voting is based on procedures, numbers, measurements, feedback, and data. Voting is not based on not-operationally-defined essences, reifications, fears, dramas, feelings, threats, wishes, trust, authorization, belief-ness, faith, tradition, habit, permission, labels, etc. A vote is like a physical piece of machined metal; A vote exists or does not exist with the measurable features that it has, and these measurable features are and must be measurable and confirm-able by anyone who measures it. Any group of people who carry out the math-science-data process of sound voting have performed voting in a way that can be audited and measured and published. No group of people can skip or shortcut required math-science-data processes without having skipped those required math-science-data processes. As with a surgeon washing their hands before surgery, "trust" is a term better used to mean that you trust the surgeon is following best practice, though even then probably it is best to simply verify without trust. But under no circumstances can 'trust' replace or permit the skipping of required processes for people or groups however much they demand and violently enforce their unfounded exemption from required best practice. In other words, if a person or group says "You MUST trust me, so I do NOT need to wash my hands before performing surgery on you or processing your vote in a best practice auditable way", you are by definition being subjected to violence, coercion, fraud, and classically defined tyranny.


# Proposed Steps for Secure Online Voting

Rule 1: Problems must be solved in-person with the voter present and with that voter's proof of identification in the same way that the person would register to vote (and/or cast their vote in an in-person election).  


Step 1: (During in-person registration) 
Before the election ends: A person, e.g. in-person, with ID (identifiable as an eligible voter according to local rules), goes to the Voting-Office to register for the vote-over-a-network (with One-Time-Pad) (online voting) process. 

(Note: There is a system-design-choice to allow (or not) registration for more than one election. This issue can be related to the format/type of the submitted ballot. For example: 
#### A. ballots that have been (or can have been) designed at the time of registration, and 
#### B. Standardized or truncated ballots containing just choices and not all the text of the ballot (possibly a choice (e.g. choice number) and the initials of the person's name as a second factor) and 
#### C. whether whatever form of ballot is customized for each voter (e.g. with a custom-id, verifiable as going to and coming from that one voter) or whether the ballot is standardized (and verifiable as the standard ballot for that election or more standardized) )

Step 2: (During in-person registration: Make one-time-pads.) 
For a given single vote-ballot in a given single election (note: multiple is another design option) there need to be four physical paper documents. One "pad" (as defined here) is two identical paper documents, one for each party (two parties, in this case: 1. The Voter and 2. The Vote-Office). Since there will be two "exchanges" (one (1) where the blank-ballot is sent to the voter, and another (2) where the filled-in-ballot is sent by the voter to the vote-office), there need to be two pads. E.g. If the voter obtains a ballot from a compromised public ballot website or a fake website (disinformation) then that vote may be disrupted.

(Alternately the voting-system could be streamlined to use only one pad for submitting a standardized public ballot, but this shorter process does not include the step for the voter to confirm that the ballot was sent by the vote-office and it also prevents the office from confirming that the ballot used was the same ballot sent by the vote-office to the voter. See below for more details.) 

The additional step of having two pads (one being to send the voter a ballot) and not just one pad to inspect that ballot coming in has several advantages. This allows the voter to verify that the ballot they are filling out comes from the Vote-Office at which they registered, and that only someone with physical access to the physical one time pad created at their time and place of registration has sent them this ballot. This allows for a comparison by the Vote-Office, likewise, of the ballot sent and the ballot received. The benchmark for success here is to be as secure as in-person all-paper voting. Just as it is possible (in theory) for a hostile group to physically take over a Vote-Office and issue people fake ballots, or send people fake mail-in ballots in the mail, this one-time-pad-vote-by-network proposal does not prevent such physical attacks on physical paper voting infrastructure. It does however create an extra layer of verifications that can be used during and after the vote takes place, which in theory could also be used to security-harden an all in-person all-paper voting process to make it more secure and auditable. (Note: Another additional or alternative method for some of these checks may be cryptographic signing (with optional multiple signatures) from trusted authorities (Vote-Office, federal or state agency, universities, 3rd party certifiers, etc). 


During the in-person one-time-pad-voter-registration: Two physical copies (e.g. QR codes printed on paper) of two one-time-pads are created; one set of the two pads are stored (offline) by the local Vote-Office, the other set (pair) of one time pads is kept by the voter themselves (physically, offline).

The software will print the one-time pads. The software will check (confirm, verify) the one-time pads. The software will erase thoroughly from memory (e.g. physically overwrite) any record of what the printed one-time-pads were.
(Note, if this process is done off-line using a dedicated machine, the risk (attack-surface) of someone being able to take (exfiltrate) the one-time-pads is reduced. Especially if the custom machine does not have enough memory to store any old pads but can only process and re-write-over one pad at a time.)

Step 3: (During in-person Registration: Create Encrypted Ballot) 
For the voting-office to send one ballot to one voter:
The election office, offline (enforced by software), uses the first 1:2 of the pair of printed QR codes to create an 'encrypted' version of the ballot for that one voter. 
Note: The ballot may be public, but it still needs to be verified. This illustrates the "verification" role sometimes lumped together with "security" and "encryption." The emphasis is not on 'hiding' the public ballot form, but on verifying that the specific ballot form that the voter is filling out is (identical to) the form that the local election office gave them.

Notes: It may be desirable to have a 'verified public ballot' as opposed to a 'private ballot' which in theory could vary (for security and verification) from the standard public ballot (in a context of mapping out a potential attack space). 
In the case that a truncated-submitted ballot is used, some way may be desired to, e.g. make a short hash of the original ballot itself (e.g. to convert the ballot by OCR or perhaps have a QR code on the ballot (though a QR on a ballot received by a voter code could be forged, whereas a hash made by the voter of the whole ballot could not be). Perhaps having a multi-pass OCR hash of a public ballot submitted with the vote to indicate that the correct ballot was used (again, in the case of a truncated submission, for a full ballot return the whole ballot is there)(also see asymmetric signing keys). 
It may be possible to have both a public verified 'open' ballot format and some unique element for the voter to check that the ballot comes from the Vote-Office with the voters one-time-pad (such as a unique id code at the bottom or top of the ballot)


Step 4: (Sending out the not-yet-completed ballot to the voter) 
During the election period (be that months, weeks, days, hours, etc.), a one-time-pad 'encoded' ballot is sent [from the voting-office to the voter] by whatever agreed upon ("electronic" or non-paper) method (website, email, SMS-text, mobile-app, S3, api-endpoint, etc.) in the form of a QR code.

Note: As an example method for a 'personalized ballot,' a randomized process of frame-shifting the ballot so that where exactly on the page each person's vote-choices appears is random, increasing the entropy of the unique ballot (e.g. so that the voting-office can increase confidence that the ballot they receive back from the voter is the one they set). 

Step 5: (Receive the not-yet-completed ballot) 
Using one piece of software, the voter offline (enforced by software, possibly hardware) 'decrypts' the ballot and then physically prints the ballot.

(Note: There is a choice here between using a public standardized ballot or a per-person ballot (e.g. with a unique id number or such, to verify that the ballot-form sent was the same as that received, or a short-form vote which contains just the choices and not all the text of the ballot.)

Step 6: (Validate the not-yet-completed Ballot) 
The voter off-line(enforced by software), inspects and validates that their digital scanned version of their not-yet-filled-out-ballot is the correct ballot-form intended for that election (e.g. not a tampered with or accidentally incorrect ballot). There are various and possibly multiple ways to check this (elaboration pending).

(Note on Steps 5 and 6: possibly the validity of the ballot could or should be checked during both steps)

Step 7: (Complete the Ballot, Mark Votes) The voter, off-line(using pen and paper), fills out the ballot (selecting their vote choices). (Details here may be important in some way: filling in a circle, selecting an option number, multi-factor, non-over-under-voting checks, etc.)

Step 8: (Digitize the Completed Ballot) 
The voter, offline (enforced by software), scans (e.g. by taking a picture) the completed-filled-in paper ballot, creating not a photo but a document or table of information (so that the one-time-pad can convert character by character). 
(Note: maybe some kind of mono-space font and dashes between lines to avoid spacing errors?)

~ Step: An optional intermediate step here is to have a 3rd set of offline-only software that will check the ballot before and or after it is filled out by the voter, such that this additional set of software can check for the "overvoting" (voting for both candidates) and "undervoting" (voting for neither candidate) issues as a safeguard (against accidentally-incorrectly filled-out-and-submitted ballots) and that perhaps Nevada has used successfully. 

Reference:
See: 
"Roll Off at the Top of the Ballot: Intentional Undervoting in American Presidential Elections"
December 2003 Politics & Policy 31(4):575 - 594
DOI:10.1111/j.1747-1346.2003.tb00163.x
Authors: Stephen Knack & Martha Kropf
University of North Carolina at Charlotte
https://www.researchgate.net/publication/227617394_Roll_Off_at_the_Top_of_the_Ballot_Intentional_Undervoting_in_American_Presidential_Elections 

Another 'multifactor' check may be to both indicate a choice and give some information about that choice, e.g. option 2 and the first letter of that candidate's last name. If these do not match, the voter should be alerted to check their ballot selections.
The voter, offline(enforced by software), scans (e.g. by taking a picture) the filled-out paper ballot. 

Step 9: (Check Completed-Ballot for Errors) 
The voter confirms that the information in their (the voter's)  electronic scanned ballot is the same as the paper version of their (the voter's) filled out ballot. (Checking for errors.) (Note: Automated processes for checking ballots for standard mistakes.)

Step 10: (Encrypt the Ballot) 
The voter, off-line(enforced by software), uses the one-time-pad to 'encrypt' the completed ballot, producing a new QR code (which is then 'encrypted' ballot). All digital files of the unencrypted ballot are removed and the memory physically over-written on the voter's device. The paper copy of the voter's ballot can be saved for evidence or destroyed for privacy based on the voter's choice. (Note: signing signatures can be used with the printed ballot or QR-code to increase confidence that the ballot is authentic. This combines advantages of asymmetric encryption along with a physical printed paper trail for audits.)

Step 11: (Submit encrypted-ballot over network) 
Online: The voter sends their completed-ballot-QR-code (containing the voter's encrypted filled-in and checked ballot) to the local election office (sent by whatever agreed upon method (website, email, text, messaging software, shared storage (e.g. S3), api-endpoint, etc.)).

Step 12: (Processing the voter's encrypted ballot)
The local election office physically prints onto paper the QR code for the 'encrypted' filled out ballot, and then (double) checks (compares) to confirm that the physical print (of the electronically-sent QR code) is accurate/identical, and (if printing is accurate) deletes the digital record and the memory is physically over-written.
1. Print
2. Check
3. Delete

Step 13: (Processing the Voter-Submitted Ballot)
Offline, using a separate piece of software, the local election office "decrypts" the QR code for the 'encrypted' completed(choices-filled-in) ballot using the second(2:2) of the pair of printed (pad)QR codes for the one-time pad, and physically prints on paper the voter's filled-in ballot. 
(Note: one choice in designing the software is to directly-print-to-paper or to decrypt and display on a screen or possible save as a computer file)
The voter's completed ballot is stored along with any completed paper ballot (e.g. mail-in ballots, or paper ballots delivered in person or filled out in person).
(Note: depending on the details, an additional step may be needed to convert the format of the QR code (or abridged format) to the same format as an in-person ballot. For example, if only the vote choice data are recorded in the QR code (or abridged format) the exact placement of each printed character on paper may be needed or useful for manual or automated ballot counting).

Note: if the ballot is processed on an off-line not-connected to a network computer then the chances of 'hacking' the vote are reduces (the 'attack surface' is reduced). 

Step 14: (Process Election Data / Count The Votes)
The printed ballot is counted with the other paper ballots of various kinds during the normal election ballot count process.

Step 15: (Publish Election-Results Data)
The election results are processed and published.
(The publication of election results is perhaps not strictly part of the question of 'secure voting' but in practice it is likely often a requirement.)


Note: Someone may wish to save a QR code (or equivilent) as some form of record. There is no security need to carefully dispose of used QR codes after they is used because they are only used once; for example obtaining an old QR code (one time pad) will not in any possible way help to "decrypt" another future one-time-pad, one-time-pads are not similar to passwords in this way (leaking archived passwords would likely be considered some form of security breach, whereas accessing already disposed of QR codes is useless; literally a set of random  numbers that won't help anyone to do anything elicit, this is the point and function of a one-time-pad). 


# Identifying Risks 
Here we look at risks from bad-actors or bad-agents. A bad-agent may be human or automated, may be local or non-local agents such as foreign states / groups. (As of 2022 ransomware is popular, and it is possible that an election system could be targeted e.g. for ransom, so designing a distributed and attack resistant framework may be important.)
An 'agent' may be anything from a single person to a group to an AI-bot or software suit, malware, ransomware, thinktank, etc. (or something unclear and not simple to identify) (note: other areas of risks should be explored, and may include: 1. constant 'internet background radiation,' 2. unintentional user-misuse 3. unintentional administrative bungling, 4. oversights and biases (e.g. setting up a voting system and obsessing so much over absolutely obscure vote secrecy that vote auditing and best practice domestic and international observation of the vote process is impeded, impracticable, or impossible), 5. practical feasibility vs. ideals in principle (possibly similar to "letting the perfect be the enemy of the good') 6. software design problems that cause time, logistical, or reliability problems, 7. etc.)

1. a bad-agent will intercept one-time-pads:
1.1 - the agent would need to be physically in the room during the QR code creation, to break into the gov. office, or to physically steal from the person, without anyone knowing the QR codes were stolen. 

1.2 - the one-time-pads are never stored digitally anywhere, but are only physically printed by an off-line computer.
1.3 - if the voter loses the QR code the person should cancel the process

2. a bad-agent will send the voter a fake blank-ballot:
- additional step: there can be additional checks such as a passphrase chosen by the person which could not be electronically surveilled from any computer (e.g. written in pen on the QR pad) 

3. a bad-agent will send the gov. a fake filled-in ballot:
- 3.1  The bad-agent would need to have both stolen QR codes and a stolen ballot that was sent to the voter.
- 3.2  If the voter loses the QR code the person should cancel the process.
	
4. a bad-agent will record a fake record of the vote from the ballot:
- while a possible risk, this process is the same as for any paper ballot

5. a bad-agent will act on the behalf of a participant without the voter's participation
- cast a vote
- cancel or change registration
- try to register or get registration information

6. a bad-agent will act on the behalf of the voting office without the voting-office's participation

7. a bad-agent will attempt to tamper with a public ballot (e.g. a ballot itself, e.g. downloading a ballot to use)

8. a bad-agent will attempt to tamper with public ballot-confirmation information (e.g. public information posted about the ballot by the voting office, describing and understanding the ballot and ballot issues)

9. a bad-agent will attempt to tamper with voting instructions and information about voting procedures

10. a bad-agent will attempt to tamper with vote reporting including any information put out by a Vote-Office or similar authority

11. a bad-agent will seek to disrupt the sending and receiving of vote information (including but not restricted to blank and filled-in ballots (e.g. voting times, places, registration, ballot items, etc). 

12. a bad-agent will participate in general or specific disinformation attacks that negatively impact the overall voting and election processes and systems. 

13. a bad agent may try to disrupt or disperse the population or geography of a vote (creating a need for refugee voting). 


# Description Notes:
This is a proposed process for reasonably secure 'online (over a network) voting.' Part of this design is that the entire process is not on-line. Rather, physical printed materials and off-line computers are used to reduce the online attack surface. A person or bad-agent can feasibly steal or tamper with a file in a network-connected computer from a remote location, but a person or bad-agent cannot feasibly/easily tamper with or steal documents in a filing cabinet or from a computer connected to the internet. This particular solution is not a perfect-for-all-cases solution. E.g. This will not be easy to use for persons who cannot ever travel themselves to a gov. office or polling place. 

The primary focus of this report is the question of whether casting a ballot/vote over-a-network(online) can in principle be done with sufficient security and soundness. Secondarily, this report explores 'practical and thrifty' variations which add in factors of feasibility, cost, equipment availability, and other real-world factors that communities around the world may face in actually holding an election (i.e. not everyone has ideal funding and resources with which to carry out the perfect election). Another way to look at this distinction is that we first look at an ideal voting system to aim for, and then look at realistic voting systems. 


# Implementation Notes:
These are recommendations for a reasonably secure online voting system that should not be significantly more cumbersome than a physical paper voting system. 

To make accessibility easier, it is conceivable that some local voting systems would prefer to simplify some of the security step to allow broader accessibility:
- voters who have no access to a printer
- voters who cannot physically travel (e.g. elderly persons in retirement home or hospital), perhaps allowing a proxy to carry documents for that person. 

Additional steps could also be taken to increase the security further. 
#### For example: 
1. to reduce the possibility that local staff will accidentally connect to the internet or run the software on insecure or already compromised hardware, it should be possible to create a cost effective system where staff could run a custom made operating system (custom BSD or Linux or FreeDOS, etc) that lacks the ability to use the internet. It may also be possible to use cost effective hardware such as a $40 raspberry pi computer. 
2. Put safeguards into the software to at least try to prevent using the same one-time-pad more than once. 

## Unique Ballots:
At this time or at a later time (depending on choice, timing, etc. (e.g. if the ballot has been decided which is often not the case at the time of voter registration or if in terms of security level if the voter does not trust a physical breakin of the vote office and wants in advance a verifiable ballot) (offline) a printed copy of a unique ballot (e.g. containing if not the voter's name the equivalent of a sha256 hash of the unique ballot). Either a unique ballot or a unique ballot identification number will be used on both ends, by the voter to check that the ballot they receive is authentic and by the office that the ballot received completed and sent by the voters is authentic. (Note: some combination of a 'signed' public ballot and a signed sender/recipient may also be possible)


## Challenges:

One possible area that may cause issues is if the office or voter is 'unable' to scan or take a clear photo of the document, in the same way that some people are 'unable' (which ranges from people having legitimate handicaps to people not bothering to try) to take a clear picture of their check for their bank (so a less secure non-printed option may be desired in some cases).
It is also possible that OCR (optical character recognition) may not be good enough to read the ballot, but given the use of OCR to read more obscurely printed checks etc., this is probably not a terminal obstacle. 

The task of automated ballot-reading perhaps should be steered away from subtle character recognition of natural-language phrases and towards clear easily defined targets such as binary check-box selection. An exception to this may be write-in ballots which do occur, where some other system may be needed (binary as in: checked-box vs. not-checked-box).
Though even here, OCR and having the vote double-check to see that the OCR is correct may be sufficient. 


# About One Time Pads
A one-time-pad is not the same as a re-use-able 'code.' A re-use-able code 'encodes' a signal and is re-used, such that 'breaking the code' will allow decrypting the document. A one-time-pad is different. A one-time-pad is not such a 'code.' A one-time-pad is a one-for-one set of changes for every character in the document, each completely random, with no pattern, and the one-time-pad is used only one-time. Even in principle you cannot 'break' a one-time pad however much you examine the encrypted document (unless the one-time-pad itself is somehow extremely defective).  Unfortunately, the terminology can be overlapping and a bit unclear between the two. For example, the terms 'encode' and 'decode' may be used in both cases, and the overall process and purpose is usually similar or the same. 

A 'one time pad' historically was literally a pair of identical physical note-pads (the same set of characters on pages 1,2,3 etc. of both notebooks, like two copies of the same book (like two identical copies of Alice in Wonderland, with the same characters on the same numbered page of each book), where each page of which was used one time, hence the term "one-time-pad."

With a one-time-pad, every character or element or number of the entire document is individually substituted for something else. There is no pattern or system behind a one-time-code that can be outsmarted or 'cracked.' The only way to 'decode' a one-time-pad 'encrypted' message is with that one-time-pad; a one-time-pad is a one-by-one, one-for-one, one character at a time, change of what the original text says. There is no key. There is no password. There is no shortcut. Every character or element or number of the entire document is individually substituted for something else. 

One-time-pads codes are not as efficient and user friendly as 're-use-able' codes in some ways, but they are more secure and more simple. Because there is no 'key,' there is no possibility in principle to 'guess the key.' 

...

Q: Is there a lower-tech version with reasonable security for geographic locations with limited resources?



# Part 2: Practical Secure Online Voting
### A pragmatic version of online voting for realistic practical implementation

For example, some voting locations (or regions) may not have: 
1. printers, ink, and paper
2. extra air-gapped computers
3. a physical location to securely store paper files
4. broadband wireless internet

Most locations can be assumed to have and required to have:
1. basic mobile phones
2. basic (not high speed) internet access


Writing down the numbers and confirming with a photo (no printers needed) may be able to replace a printed QR code system while still having a paper-backup form, if only as an option (e.g. you cannot hack into and change a piece of paper). 

Maybe separate air-gapped mobile devices would be feasible, or perhaps a more decentralized system would be more secure.


# An alternative thrifty-protocol for resource-limited situations/geographies: (section under construction)

## Practical Voting
The goal here (for this practical-tool section, vs. the above secure voting in principle) is more a practical-project and less abstract (proof of concept or standard-setting): How can a local community organize and carry out a best-practice auditible vote and publish the results using (widely available and) accessible technology (such as mobile phones)?

What are some of the factors that characterize a realistically resource-limited situation? Are there some general groups of common sets of constraints? E.g. Some groups may have a safe place for a voting office but no funds for extra equipment. Other groups may not have a safe place for any voting office or official positions (needing the management of the election to be virtual and decentralized). 

Question: Can virtual distributed elections be best carried out with or without support from institutions such as universities? 

Thrifty voting systems may make more use of available multi-factor authentication and less use of equipment-expensive methods (such as dedicated printing and scanning machines). 

There should be some option for physical printed documents, but there will most likely be more use of non-paper methods for a thrifty resource-slim and more user-friendly system. 

Other methods such as chains-of-trust may be useful to harden thrifty online systems.

#### General Revisions for Thrifty-Secure-Voting:
1. no physical printed copies 
2. no separate air-gapped hardware
?. one pad per set of elections vs. two pads per single election (backup pads?)
3. more cryptographic signature use?

Topic:
- use of one time pads and signing signatures



Notes:
- individual permission drop-off folders (like S3)
- anonymized ballots (storing data without direct connection to user information)
- face-picture when sending in vote
- vote by phone system, tied to that phone...(note: if you lose the phone)

Ballot format standardization?
- csv format: pads, ballots, votes

# Proposed Steps for a Practical  Secure Online Voting (section under construction)

Note: This thrifty and pragmatic (if not perfect) system does not assume there is a voting office either as a building or as human staff.

Step 1: (During online registration) 
Before the election ends: A voter registers for the vote-over-a-network (with One-Time-Pad) (online voting) process. 
This may be done entirely online for most-practical voting, or other elements may be added.

For entirely-online-voting there is the challenge of selecting who on the internet may participate. 
A kind of hybrid may involve e.g. sending snail-mailed to voters (or picked up with ID from an office) to use to authenticate their online connection. 
note: using signing signatures,


Step 2:

While the thrifty-protocol is designed to avoid extra printer hardware, the option still exists to hand-write a one-time pad. 
A short-form ballot one time pad good for several ballots may be hand written and OCR-checked on a wallet-card sized card or paper.

A short-form or truncated ballot may contain, e.g., the number of the option-choice and perhaps a first/last letter in the candidates name (which could also serve as a check, similar to an empty choice check, if the name-letter does not agree with the number option). Two-factor-no-nul voting?
Note: Write-in may be an issue for the truncated ballot. 


Note: ways to make sure a one-time-pad is not being used a 2nd time...a log of already used one-time-pads to check against...?...or a small hash?

Step 3: (this step needed for thrifty-version?)(extra other steps?)
Q: one time pads vs. signing keys for transmitting ballots



Step 4: (send ballot?)
3 options:
1. a publicly posted signed ballot (verifiable)
2. a ballot including a unique personal id sent only to that one person 
3. both

During the election period (be that months, weeks, days, hours, etc.), a one-time-pad 'encoded' ballot is sent by whatever agreed upon method (website, email, text, snapchat, S3, api-endpoint, etc.) in the form of another QR code.
Part of this process is an at-the-time randomized process of frame-shifting the ballot so that the location on the page where each person's vote-choices appear is random. 

Step 5: (Voter Gets the not-yet-completed ballot)  
A. sent to user
B. posted on several public sites and signed and can be compared/verified

Step 6: (Voter Validate the not-yet-completed Ballot) 
The voter on-line inspects and validates the ballot. Most likely by checking and comparing multiple sources and signing keys.
(note: finding universities to host copies of the final ballot may be a good option. But this step may not be feasible or necessary.) (Something like a blockchain (immutable ledger) for all users of the voting system may suffice as a good-enough decentered immutable portable verified storage system.)


Step 7: (Complete the Ballot, Mark Votes) 
e.g. csv format of data (vs. pdf type doc)
Q: id such as biometric data

~ step: an optional intermediate step here is to have a 3rd set of offline-only software that will check the ballot before and or after it is filled out by the voter, such that this additional set of software can check for the "overvoting" (voting for both candidates) and "undervoting" (voting for neither candidate) issues as a safeguard (against accidentally-incorrectly filled-out-and-submitted ballots) and that perhaps Nevada has used successfully. See: 
"Roll Off at the Top of the Ballot: Intentional Undervoting in American Presidential Elections"
December 2003 Politics & Policy 31(4):575 - 594
DOI:10.1111/j.1747-1346.2003.tb00163.x
Authors: Stephen Knack & Martha Kropf
University of North Carolina at Charlotte
https://www.researchgate.net/publication/227617394_Roll_Off_at_the_Top_of_the_Ballot_Intentional_Undervoting_in_American_Presidential_Elections 

Step 8: (this step needed for thrifty-version?)(extra other steps?)

Step 9: (Check completed-ballot for errors) 
(see step 7?)

Step 10: (Encrypt the Ballot) 
Q: if an anonymized blockchain system is used, is there a need to encrypt the submitted ballot?

Step 11: (Submit encrypted-ballot over network) 
Q: recommended methods?
some kind of MFA or blockchain ledger system?

Online: The voter sends (by whatever agreed upon method (website, email, text, snapchat, S3, api-endpoint, etc.)) the new QR code (containing their encrypted filled-in-and-checked ballot) to the local election office.

Step 12: (Processing the encrypted Voter-submitteds ballot)
- thrifty encryption choice?

Step 13: (Processing the Voter-submitted ballot)
- format of ballot
(csv?)
(voter checks on status?)

Step 14: (Process Election Data / Count The Votes)
(storage: block chain or other immutable ledger?)

Step 15: (Publish Election Data)


(election results publishing...parts of process)

Note: It is not clear that saving the QR codes serves any function, nor is there any need to carefully dispose of a QR code after it is used (if each is only used once). 

What kind of software (singular or plural) would be needed to arrange a secure election?

Immutable-Ledger Data-Structures: Could some form of blockchain constructed by election participants be used as a decentered election results platform? 

Part of an online system may be to increase the number of channels by which people can try to vote, and possibly have a backup-pad. Thereby, if bad-agents shut down the main channel for sending in votes (which may be a single point of failure) the process will not be disrupted.


# A Practical Election Management Package

#### Features of a practical voting software package:
1. secure messages between office and voter? (one time pad?)
2. secure voting platform (receive ballot)
2.1 voter registration
2.2 send or assign ballots
2.3 fill out ballot
2.4 submit ballot
3. Processing votes
3.1 receive votes
3.2 validate votes
3.3 decrypt votes
5. process votes
6. produce results report
7. schedule election
8. publish results report

Mode 1: single physical vote office

Mode 2: meta-population of physical vote offices

Mode 3: remote vote office(s)

Mode 4: decentralized vote office (distributed among voters)

Maybe each 'election' will have a different signing key to verify?

software platforms/languages:

Project:
"Pseudocode for voting infrastructure"
- including how to create randomized representative voting districts
- including how to do ranked choice voting
- including how to do (term) ? representational voting

- boundaries of population and geography of vote

- (make) rules for voter participation/qualification in an automated voter system



# (mitigation of insecure local voting headquarters)
2nd step of recording / publishing vote:
Uuid type random key-field
Fuzzy time stamp (month year?) unix epoch


2. Using a modified blockchain to store results:
- e.g. university trusted node anchors
- maybe full-chain so no retroactive?
- slower but more robust?
- smaller number of participants? (or pooled participants?)
- containing hash and voting record?





....

Possible Multi-factor Authentication Tools:
1. voice print
2. picture of hand (for fingerprints)
3. one time pad
4. specific device tracking
5. device gis location
7. ip / mac address details (vpn issues?)
6. separate confirmation login (to confirm vote record (device, voice, etc.) after it has been processed and recorded)
7. face-selfie (time GIS stamped picture of person casting vote)
8. video of person voting (more secure than static selfie?
or smaller-file 'encoding' (e.g. auto-encoder) of video of person voting

(plus)
1. public security log data/meta-data to be inspected by anyone about the system
 

## Additional Questions:
1. What additional vote process transparency information should be included with vote results publishing? 
https://github.com/lineality/Auditable_Elections_Projects


...

Case Studies in Election Disruption and Resilience:
- 
- 
- 

Case Studies in Disrupted and Problematic Elections:
- 
- 
- 



...

## A Voting Rules And Procedures Statement

As part of an election, other publicly stated 'open' policy and procedure information is important in addition to the ballot itself.

- rules, policies, and procedures for how rules, policies, and procedures for voting are made, unmade, and changed
- time and data on opening and closing of poles for a given election
- times places methods for ways of voting allowed
- rules, policies, and procedures schedule for repeating elections
- specific schedule for repeating elections (e.g. this is a run-off vs. this election is held every 2 years)
- rules for calling elections
- Repeating or other type of election
- Place of election
- Government Structures and Levels
- Vote-Office information (location, head?, contact, reporting?)
- Chain of Command within and above Vote-Office
- rules, policies, and procedures contacting media or watchdogs about suspicious anything (emails, threats, voter intimidation, etc.)

- rules, policies, and procedures for eligibility
- rules, policies, and procedures for voter-registration
- rules, policies, and procedures for per way to vote
- rules, policies, and procedures for election audits (required audits, optional audits)
- rules, policies, and procedures for election-results-challenge
- rules, policies, and procedures for recount (automatic recounts, type of recount, etc.)
- ules, policies, and procedures for overruling-election-results e.g. by gov. branches, evidence requirements
- rules, policies, and procedures for chain of custody of election materials, equipment, etc., Provenance   
- rules, policies, and procedures for announcing and publishing results 
- rules, policies, and procedures for reporting information about the vote: procedures, voter enrollment and participation numbers, etc. 
- Should there be a 'log' of who makes changes to procedures and how?
- rules, policies, and procedures for election and ballot counting observation
- rules, policies, and procedures for exit polls (what collected, from whom, released when)
- rules, policies, and procedures for meetings and correspondence transparency around voloting infrastructure and offices and resources
- rules, policies, and procedures for foreign domestic local and internal interference with the attacks on the election process
- rules, policies, and procedures for voter registration
- rules, policies, and procedures for voter identification 
- For evaluation of best practice, performance, and ethics: standards, guidelines, benchmarks and audit materials
- rules, policies, and procedures for raw vote results (including ranked-choice etc.)
- rules, policies, and procedures for choosing vote calculation method
- rules, policies, and procedures for vote calculation method (e.g. how different numbers of candidates are handled, e.g. 2 vs. not-2)
- rules, policies, and procedures for specific-used vote calculation method
- rules, policies, and procedures for the storage of records from past elections
- rules, policies, and procedures for "stateless" voting machines
- rules, policies, and procedures for election observers
- rules, policies, and procedures for auditing, vetting, and guarantors 


#### Question: A. What is the relationship between secure end-to-end messaging and voting systems? B. Provenance: What is the relationship between origin-verification of files (indlucing media files) and voting systems?


### Issue/Task: user interface for setting up an election


Q: a standardized .csv ballot format
including information about the ballot
signing key information
possible vote customization information
vote choices
etc.
Q: ways to make sure the .csv ballot is not mis-read or garbled
e.g. maybe including item number, vote choice, and first letter/number of vote choice name in the vote, may prevent arbitrary misinterpretation of votes
Q: possible requiring of ballot being completely filled out
- digital signature etc.
- checksum etc.


practical model 2:
Similar to baseline secure model with these changes:
- allows registered phone number use:
	- ballots can be exchanged by ~sms or 
	- possible voice print ID: e.g. similar to online-voter registration credentials


practical model 3:
Use of block chain ledger

practical model 4:
using nft smart contracts as a framework for parts of the election

practical model 5:
using existing online registration systems

A note on election security and registration security: 
Does it make sense to have lower security standards around registration for voting than casting of votes? A similar or perhaps identical question is: Does it make sense to have a less security system for registration than for voting? E.g. in Pennsylvania in 2022 you can register to vote and change your party-registration, address, etc., on a simple website with no additional security, no MFA multi factor authentication, no personal in face verification, no biometrics, no mailing address sent verification, etc. And I have never heard anyone complain about the insecurity of this registration system, and a proposal to use the same system for voting immediately results in a vitriolic hyperbolic uproar of arm-waving indignation. Personally I think online registration should be more secure. My overall point here is that both registration and voting should be discussed and implemented as they relate to each-other, and not treated as if they are unrelated with inconsistent security considerations. If the standard for security is good enough for registration, that should be the same standard for voting.


# Voting, Contracts, and Smart Contracts:
What are the feasible properties of smart contracts that relate to elections, either for their use in a particular situation or as a discussion to elucidate needs and functions?


# voting office setup: Computer, OS, and Network security
What OS, what network architecture, and what cyber security strategies should/could voting offices use?
- topic: stateless machines
- topic: air-gapped machines
- topic: not-networked Operating Systems
- topic: memory throttling 


# Standards and Measures
- file types
- data types
- calculation methods
- statistical methods 
- disclosure of methods

# Advantages of an anonymized public ledgers of votes:
-

....

# Auditing Election Processes (vs. specific elections):
- operationally defining problems with election procedures
- processes for finding local consensus or agreement on areas of trade-off compromise, or ambiguity (identification, registration, voting age, duration of vote being open, campaign finance, etc.)
- cross regional and international audits

....

# Overall Discussion:

- Why are specific technologies used for voting? 

- What is different about 'electronic,' 'network,' and data structure technologies? (making them appropriate or inappropriate for voting systems)

- In the timeline of technologies, which technologies are appropriate and inappropriate and why?
- (e.g. complete census vs. statistical sampling)



# Tradeoffs in Voting:
- accessibility vs. security
- smaller attack space vs. fancy interface
- direct vs. representation
- 

# voting and principles of security (ease of use vs. security etc)
- 

note: RC4 used correctly



Improvised Network in case of public internet disruptions:
- 
