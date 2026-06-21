"""Generated from Smithy shape ``com.amazonaws.ecr#SigningStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The image signing status. Possible values include <code>IN_PROGRESS</code>, <code>COMPLETE</code>, and <code>FAILED</code>.</p>"""
SigningStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SigningStatus:
    return cast(SigningStatus, data)
