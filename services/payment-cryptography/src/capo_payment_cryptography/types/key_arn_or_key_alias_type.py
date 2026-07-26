"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#KeyArnOrKeyAliasType``."""

from typing import TypeAlias

"""<p>A key identifier that can be either a key ARN or an alias name. This allows flexible key identification in operations.</p> <p>When using a key ARN, it must be a fully qualified ARN in the format: <code>arn:aws:payment-cryptography:region:account:key/key-id</code>.</p> <p>When using an alias, it must begin with <code>alias/</code> followed by the alias name.</p> <important> <p>Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>"""
KeyArnOrKeyAliasType: TypeAlias = str
