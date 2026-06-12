"""Generated from Smithy shape ``com.amazonaws.voiceid#UpdateDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain


class UpdateDomainResponse(TypedDict):
    domain: NotRequired["aws_sdk_voice_id.types.domain.Domain"]
    """<p>Details about the updated domain</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDomainResponse) -> dict:
    out: dict = {}
    if "domain" in value:
        import aws_sdk_voice_id.types.domain

        out["Domain"] = aws_sdk_voice_id.types.domain.serialize_aws_json_1_0(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDomainResponse:
    out: UpdateDomainResponse = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        import aws_sdk_voice_id.types.domain

        out["domain"] = aws_sdk_voice_id.types.domain.deserialize_aws_json_1_0(
            data["Domain"]
        )
    return out
