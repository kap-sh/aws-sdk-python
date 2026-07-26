"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CertificateAuthorityBody``."""

import base64
from typing import TypeAlias

CertificateAuthorityBody: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthorityBody) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> CertificateAuthorityBody:
    return base64.b64decode(data)
