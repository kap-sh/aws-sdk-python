"""Generated from Smithy shape ``com.amazonaws.voiceid#DescribeFraudsterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.fraudster_id


class DescribeFraudsterRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the fraudster.</p>"""
    fraudster_id: "aws_sdk_voice_id.types.fraudster_id.FraudsterId"
    """<p>The identifier of the fraudster you are describing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFraudsterRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["FraudsterId"] = value["fraudster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFraudsterRequest:
    out: DescribeFraudsterRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("DescribeFraudsterRequest.domain_id required")
    if "FraudsterId" in data:
        out["fraudster_id"] = data["FraudsterId"]
    else:
        raise DeserializationError("DescribeFraudsterRequest.fraudster_id required")
    return out
