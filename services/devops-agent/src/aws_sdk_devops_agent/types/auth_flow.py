"""Generated from Smithy shape ``com.amazonaws.devopsagent#AuthFlow``."""

from typing import Literal, TypeAlias, cast

"""<p>Authentication flow type for operator app.</p>"""
AuthFlow: TypeAlias = Literal[
    "iam",
    "idc",
    "idp",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthFlow) -> str:
    return value


def deserialize_json(data: str) -> AuthFlow:
    return cast(AuthFlow, data)
