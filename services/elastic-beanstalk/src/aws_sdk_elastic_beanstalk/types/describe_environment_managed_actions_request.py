"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeEnvironmentManagedActionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.action_status
    import aws_sdk_elastic_beanstalk.types.string


class DescribeEnvironmentManagedActionsRequest(TypedDict):
    environment_name: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>The name of the target environment.</p>"""
    environment_id: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>The environment ID of the target environment.</p>"""
    status: NotRequired["aws_sdk_elastic_beanstalk.types.action_status.ActionStatus"]
    """<p>To show only actions with a particular status, specify a status.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEnvironmentManagedActionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "environment_name" in value:
        pairs.append((f"{prefix}.EnvironmentName", str(value["environment_name"])))
    if "environment_id" in value:
        pairs.append((f"{prefix}.EnvironmentId", str(value["environment_id"])))
    if "status" in value:
        import aws_sdk_elastic_beanstalk.types.action_status

        aws_sdk_elastic_beanstalk.types.action_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_query(el: Element) -> DescribeEnvironmentManagedActionsRequest:
    out: DescribeEnvironmentManagedActionsRequest = {}  # type: ignore[typeddict-item]
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_elastic_beanstalk.types.action_status

        out["status"] = aws_sdk_elastic_beanstalk.types.action_status.deserialize_query(
            child_status
        )
    return out
