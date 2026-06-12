"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DeleteApplicationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.terminate_env_force


class DeleteApplicationMessage(TypedDict):
    application_name: "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application to delete.</p>"""
    terminate_env_by_force: NotRequired[
        "aws_sdk_elastic_beanstalk.types.terminate_env_force.TerminateEnvForce"
    ]
    """<p>When set to true, running environments will be terminated before deleting the application.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteApplicationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    if "terminate_env_by_force" in value:
        pairs.append(
            (
                f"{prefix}.TerminateEnvByForce",
                "true" if value["terminate_env_by_force"] else "false",
            )
        )


def deserialize_query(el: Element) -> DeleteApplicationMessage:
    out: DeleteApplicationMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        raise DeserializationError("DeleteApplicationMessage.application_name required")
    child_terminate_env_by_force = el.find("TerminateEnvByForce")
    if child_terminate_env_by_force is not None:
        out["terminate_env_by_force"] = (
            child_terminate_env_by_force.text or ""
        ).lower() == "true"
    return out
