"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#RestartAppServerMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.environment_id
    import capo_elastic_beanstalk.types.environment_name


class RestartAppServerMessage(TypedDict, closed=True):
    environment_id: NotRequired[
        "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the environment to restart the server for.</p> <p> Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>"""
    environment_name: NotRequired[
        "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment to restart the server for.</p> <p> Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RestartAppServerMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "environment_id" in value:
        pairs.append((f"{prefix}.EnvironmentId", str(value["environment_id"])))
    if "environment_name" in value:
        pairs.append((f"{prefix}.EnvironmentName", str(value["environment_name"])))


def deserialize_query(el: Element) -> RestartAppServerMessage:
    out: RestartAppServerMessage = {}  # type: ignore[typeddict-item]
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    return out
