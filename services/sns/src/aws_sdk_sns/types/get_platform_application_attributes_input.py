"""Generated from Smithy shape ``com.amazonaws.sns#GetPlatformApplicationAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.string


class GetPlatformApplicationAttributesInput(TypedDict, closed=True):
    platform_application_arn: "aws_sdk_sns.types.string.String"
    """<p> <code>PlatformApplicationArn</code> for GetPlatformApplicationAttributesInput.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetPlatformApplicationAttributesInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append(
        (f"{prefix}.PlatformApplicationArn", str(value["platform_application_arn"]))
    )


def deserialize_query(el: Element) -> GetPlatformApplicationAttributesInput:
    out: GetPlatformApplicationAttributesInput = {}  # type: ignore[typeddict-item]
    child_platform_application_arn = el.find("PlatformApplicationArn")
    if child_platform_application_arn is not None:
        out["platform_application_arn"] = str(child_platform_application_arn.text or "")
    else:
        raise DeserializationError(
            "GetPlatformApplicationAttributesInput.platform_application_arn required"
        )
    return out
