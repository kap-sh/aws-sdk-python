"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ScheduledActionAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.scheduled_action_name


class ScheduledActionAssociation(TypedDict, closed=True):
    namespace_name: NotRequired[
        "capo_redshift_serverless.types.namespace_name.NamespaceName"
    ]
    """<p>Name of associated Amazon Redshift Serverless namespace.</p>"""
    scheduled_action_name: NotRequired[
        "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName"
    ]
    """<p>Name of associated scheduled action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledActionAssociation) -> dict:
    out: dict = {}
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "scheduled_action_name" in value:
        out["scheduledActionName"] = value["scheduled_action_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduledActionAssociation:
    out: ScheduledActionAssociation = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "scheduledActionName" in data:
        out["scheduled_action_name"] = data["scheduledActionName"]
    return out
