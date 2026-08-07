"""Generated from Smithy shape ``com.amazonaws.sns#CreatePlatformApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.string


class CreatePlatformApplicationResponse(TypedDict, closed=True):
    platform_application_arn: NotRequired["capo_sns.types.string.String"]
    """<p> <code>PlatformApplicationArn</code> is returned.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreatePlatformApplicationResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "platform_application_arn" in value:
        pairs.append(
            (
                f"{key_prefix}PlatformApplicationArn",
                str(value["platform_application_arn"]),
            )
        )


def deserialize_query(el: Element) -> CreatePlatformApplicationResponse:
    out: CreatePlatformApplicationResponse = {}  # type: ignore[typeddict-item]
    child_platform_application_arn = el.find("PlatformApplicationArn")
    if child_platform_application_arn is not None:
        out["platform_application_arn"] = str(child_platform_application_arn.text or "")
    return out
