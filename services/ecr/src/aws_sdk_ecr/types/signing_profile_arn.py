"""Generated from Smithy shape ``com.amazonaws.ecr#SigningProfileArn``."""

from typing import TypeAlias

"""<p>The Amazon Resource Name (ARN) of an Amazon Web Services Signer signing profile. The ARN contains the <code>arn:aws:signer</code> namespace, followed by the region, Amazon Web Services account ID, and signing profile resource path. For example, <code>arn:aws:signer:region:012345678910:/signing-profiles/profile-name</code>.</p>"""
SigningProfileArn: TypeAlias = str
