"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplyEnvironmentManagedActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.string


class ApplyEnvironmentManagedActionRequest(TypedDict):
    environment_name: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>The name of the target environment.</p>"""
    environment_id: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>The environment ID of the target environment.</p>"""
    action_id: "aws_sdk_elastic_beanstalk.types.string.String"
    """<p>The action ID of the scheduled managed action to execute.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplyEnvironmentManagedActionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "environment_name" in value:
        pairs.append((f"{prefix}.EnvironmentName", str(value["environment_name"])))
    if "environment_id" in value:
        pairs.append((f"{prefix}.EnvironmentId", str(value["environment_id"])))
    pairs.append((f"{prefix}.ActionId", str(value["action_id"])))


def deserialize_query(el: Element) -> ApplyEnvironmentManagedActionRequest:
    out: ApplyEnvironmentManagedActionRequest = {}  # type: ignore[typeddict-item]
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_action_id = el.find("ActionId")
    if child_action_id is not None:
        out["action_id"] = str(child_action_id.text or "")
    else:
        raise DeserializationError(
            "ApplyEnvironmentManagedActionRequest.action_id required"
        )
    return out
