"""Generated from Smithy shape ``com.amazonaws.iam#thumbprintType``."""

from typing import TypeAlias

"""<p>Contains a thumbprint for an identity provider's server certificate.</p> <p>The identity provider's server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate. This thumbprint is used by the domain where the OpenID Connect provider makes its keys available. The thumbprint is always a 40-character string.</p>"""
thumbprintType: TypeAlias = str
