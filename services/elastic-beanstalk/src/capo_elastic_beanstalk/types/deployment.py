"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#Deployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.deployment_timestamp
    import capo_elastic_beanstalk.types.nullable_long
    import capo_elastic_beanstalk.types.string


class Deployment(TypedDict, closed=True):
    version_label: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The version label of the application version in the deployment.</p>"""
    deployment_id: NotRequired[
        "capo_elastic_beanstalk.types.nullable_long.NullableLong"
    ]
    """<p>The ID of the deployment. This number increases by one each time that you deploy source code or change instance configuration settings.</p>"""
    status: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The status of the deployment:</p> <ul> <li> <p> <code>In Progress</code> : The deployment is in progress.</p> </li> <li> <p> <code>Deployed</code> : The deployment succeeded.</p> </li> <li> <p> <code>Failed</code> : The deployment failed.</p> </li> </ul>"""
    deployment_time: NotRequired[
        "capo_elastic_beanstalk.types.deployment_timestamp.DeploymentTimestamp"
    ]
    """<p>For in-progress deployments, the time that the deployment started.</p> <p>For completed deployments, the time that the deployment ended.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Deployment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "version_label" in value:
        pairs.append((f"{prefix}.VersionLabel", str(value["version_label"])))
    if "deployment_id" in value:
        pairs.append((f"{prefix}.DeploymentId", str(value["deployment_id"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "deployment_time" in value:
        import capo_elastic_beanstalk.types.deployment_timestamp

        capo_elastic_beanstalk.types.deployment_timestamp.serialize_query(
            value["deployment_time"], pairs, f"{prefix}.DeploymentTime"
        )


def deserialize_query(el: Element) -> Deployment:
    out: Deployment = {}  # type: ignore[typeddict-item]
    child_version_label = el.find("VersionLabel")
    if child_version_label is not None:
        out["version_label"] = str(child_version_label.text or "")
    child_deployment_id = el.find("DeploymentId")
    if child_deployment_id is not None:
        out["deployment_id"] = int(child_deployment_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_deployment_time = el.find("DeploymentTime")
    if child_deployment_time is not None:
        import capo_elastic_beanstalk.types.deployment_timestamp

        out["deployment_time"] = (
            capo_elastic_beanstalk.types.deployment_timestamp.deserialize_query(
                child_deployment_time
            )
        )
    return out
