"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#AbortEnvironmentUpdateMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.environment_id
    import aws_sdk_elastic_beanstalk.types.environment_name


class AbortEnvironmentUpdateMessage(TypedDict, closed=True):
    environment_id: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>This specifies the ID of the environment with the in-progress update that you want to cancel.</p>"""
    environment_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>This specifies the name of the environment with the in-progress update that you want to cancel.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AbortEnvironmentUpdateMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "environment_id" in value:
        pairs.append((f"{prefix}.EnvironmentId", str(value["environment_id"])))
    if "environment_name" in value:
        pairs.append((f"{prefix}.EnvironmentName", str(value["environment_name"])))


def deserialize_query(el: Element) -> AbortEnvironmentUpdateMessage:
    out: AbortEnvironmentUpdateMessage = {}  # type: ignore[typeddict-item]
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    return out
