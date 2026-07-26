"""Generated from Smithy shape ``com.amazonaws.proton#Service``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.arn
    import capo_proton.types.description
    import capo_proton.types.git_branch_name
    import capo_proton.types.repository_id
    import capo_proton.types.resource_name
    import capo_proton.types.service_arn
    import capo_proton.types.service_pipeline
    import capo_proton.types.service_status
    import capo_proton.types.spec_contents
    import capo_proton.types.status_message


class Service(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the service.</p>"""
    arn: "capo_proton.types.service_arn.ServiceArn"
    """<p>The Amazon Resource Name (ARN) of the service.</p>"""
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service template.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the service was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The time when the service was last modified.</p>"""
    status: "capo_proton.types.service_status.ServiceStatus"
    """<p>The status of the service.</p>"""
    status_message: NotRequired["capo_proton.types.status_message.StatusMessage"]
    """<p>A service status message.</p>"""
    spec: "capo_proton.types.spec_contents.SpecContents"
    """<p>The formatted specification that defines the service.</p>"""
    pipeline: NotRequired["capo_proton.types.service_pipeline.ServicePipeline"]
    """<p>The service pipeline detail data.</p>"""
    repository_connection_arn: NotRequired["capo_proton.types.arn.Arn"]
    r"""<p>The Amazon Resource Name (ARN) of the repository connection. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html#setting-up-vcontrol\">Setting up an AWS CodeStar connection</a> in the <i>Proton User Guide</i>.</p>"""
    repository_id: NotRequired["capo_proton.types.repository_id.RepositoryId"]
    """<p>The ID of the source code repository.</p>"""
    branch_name: NotRequired["capo_proton.types.git_branch_name.GitBranchName"]
    """<p>The name of the code repository branch that holds the code that's deployed in Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Service) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["arn"] = value["arn"]
    out["templateName"] = value["template_name"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastModifiedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["last_modified_at"]
    )
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    out["spec"] = value["spec"]
    if "pipeline" in value:
        import capo_proton.types.service_pipeline

        out["pipeline"] = capo_proton.types.service_pipeline.serialize_aws_json_1_0(
            value["pipeline"]
        )
    if "repository_connection_arn" in value:
        out["repositoryConnectionArn"] = value["repository_connection_arn"]
    if "repository_id" in value:
        out["repositoryId"] = value["repository_id"]
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Service.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Service.arn required")
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("Service.template_name required")
    if "createdAt" in data:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Service.created_at required")
    if "lastModifiedAt" in data:
        import capo_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError("Service.last_modified_at required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("Service.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "spec" in data:
        out["spec"] = data["spec"]
    else:
        raise DeserializationError("Service.spec required")
    if "pipeline" in data:
        import capo_proton.types.service_pipeline

        out["pipeline"] = capo_proton.types.service_pipeline.deserialize_aws_json_1_0(
            data["pipeline"]
        )
    if "repositoryConnectionArn" in data:
        out["repository_connection_arn"] = data["repositoryConnectionArn"]
    if "repositoryId" in data:
        out["repository_id"] = data["repositoryId"]
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    return out
