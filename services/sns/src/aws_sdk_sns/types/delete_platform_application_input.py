"""Generated from Smithy shape ``com.amazonaws.sns#DeletePlatformApplicationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.string


class DeletePlatformApplicationInput(TypedDict):
    platform_application_arn: "aws_sdk_sns.types.string.String"
    """<p> <code>PlatformApplicationArn</code> of platform application object to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeletePlatformApplicationInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (f"{prefix}.PlatformApplicationArn", str(value["platform_application_arn"]))
    )


def deserialize_query(el: Element) -> DeletePlatformApplicationInput:
    out: DeletePlatformApplicationInput = {}  # type: ignore[typeddict-item]
    child_platform_application_arn = el.find("PlatformApplicationArn")
    if child_platform_application_arn is not None:
        out["platform_application_arn"] = str(child_platform_application_arn.text or "")
    else:
        raise DeserializationError(
            "DeletePlatformApplicationInput.platform_application_arn required"
        )
    return out
