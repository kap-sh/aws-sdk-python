"""Generated from Smithy shape ``com.amazonaws.sns#CreatePlatformApplicationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.string


class CreatePlatformApplicationResponse(TypedDict):
    platform_application_arn: NotRequired["aws_sdk_sns.types.string.String"]
    """<p> <code>PlatformApplicationArn</code> is returned.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreatePlatformApplicationResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_application_arn" in value:
        pairs.append(
            (f"{prefix}.PlatformApplicationArn", str(value["platform_application_arn"]))
        )


def deserialize_query(el: Element) -> CreatePlatformApplicationResponse:
    out: CreatePlatformApplicationResponse = {}  # type: ignore[typeddict-item]
    child_platform_application_arn = el.find("PlatformApplicationArn")
    if child_platform_application_arn is not None:
        out["platform_application_arn"] = str(child_platform_application_arn.text or "")
    return out
