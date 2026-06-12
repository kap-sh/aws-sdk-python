"""Generated from Smithy shape ``com.amazonaws.voiceid#DescribeDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain_id


class DescribeDomainRequest(TypedDict):
    domain_id: "aws_sdk_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that you are describing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeDomainRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeDomainRequest:
    out: DescribeDomainRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("DescribeDomainRequest.domain_id required")
    return out
