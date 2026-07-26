"""Generated from Smithy shape ``com.amazonaws.storagegateway#KMSKey``."""

from typing import TypeAlias

"""<p>Optional. The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value must be set if <code>KMSEncrypted</code> is <code>true</code>, or if <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>.</p>"""
KMSKey: TypeAlias = str
