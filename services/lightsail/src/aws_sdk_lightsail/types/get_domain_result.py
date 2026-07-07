"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDomainResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.domain


class GetDomainResult(TypedDict, closed=True):
    domain: NotRequired["aws_sdk_lightsail.types.domain.Domain"]
    """<p>An array of key-value pairs containing information about your get domain request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDomainResult) -> dict:
    out: dict = {}
    if "domain" in value:
        import aws_sdk_lightsail.types.domain

        out["domain"] = aws_sdk_lightsail.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDomainResult:
    out: GetDomainResult = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        import aws_sdk_lightsail.types.domain

        out["domain"] = aws_sdk_lightsail.types.domain.deserialize_aws_json_1_1(
            data["domain"]
        )
    return out
