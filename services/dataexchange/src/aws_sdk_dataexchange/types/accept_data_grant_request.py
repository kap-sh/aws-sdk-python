"""Generated from Smithy shape ``com.amazonaws.dataexchange#AcceptDataGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.data_grant_arn


class AcceptDataGrantRequest(TypedDict, closed=True):
    data_grant_arn: "aws_sdk_dataexchange.types.data_grant_arn.DataGrantArn"
    """<p>The Amazon Resource Name (ARN) of the data grant to accept.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptDataGrantRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AcceptDataGrantRequest:
    out: AcceptDataGrantRequest = {}  # type: ignore[typeddict-item]
    return out
