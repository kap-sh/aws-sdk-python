"""Generated from Smithy shape ``com.amazonaws.sns#ListEndpointsByPlatformApplicationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.string


class ListEndpointsByPlatformApplicationInput(TypedDict):
    platform_application_arn: "aws_sdk_sns.types.string.String"
    """<p> <code>PlatformApplicationArn</code> for <code>ListEndpointsByPlatformApplicationInput</code> action.</p>"""
    next_token: NotRequired["aws_sdk_sns.types.string.String"]
    """<p> <code>NextToken</code> string is used when calling <code>ListEndpointsByPlatformApplication</code> action to retrieve additional records that are available after the first page results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListEndpointsByPlatformApplicationInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append(
        (f"{prefix}.PlatformApplicationArn", str(value["platform_application_arn"]))
    )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListEndpointsByPlatformApplicationInput:
    out: ListEndpointsByPlatformApplicationInput = {}  # type: ignore[typeddict-item]
    child_platform_application_arn = el.find("PlatformApplicationArn")
    if child_platform_application_arn is not None:
        out["platform_application_arn"] = str(child_platform_application_arn.text or "")
    else:
        raise DeserializationError(
            "ListEndpointsByPlatformApplicationInput.platform_application_arn required"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
