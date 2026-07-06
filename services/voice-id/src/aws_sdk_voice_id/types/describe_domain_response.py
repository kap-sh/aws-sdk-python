"""Generated from Smithy shape ``com.amazonaws.voiceid#DescribeDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain


class DescribeDomainResponse(TypedDict, closed=True):
    domain: NotRequired["aws_sdk_voice_id.types.domain.Domain"]
    """<p>Information about the specified domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeDomainResponse) -> dict:
    out: dict = {}
    if "domain" in value:
        import aws_sdk_voice_id.types.domain

        out["Domain"] = aws_sdk_voice_id.types.domain.serialize_aws_json_1_0(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeDomainResponse:
    out: DescribeDomainResponse = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        import aws_sdk_voice_id.types.domain

        out["domain"] = aws_sdk_voice_id.types.domain.deserialize_aws_json_1_0(
            data["Domain"]
        )
    return out
