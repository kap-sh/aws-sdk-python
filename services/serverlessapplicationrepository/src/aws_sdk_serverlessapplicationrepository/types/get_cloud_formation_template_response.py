"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#GetCloudFormationTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string
    import aws_sdk_serverlessapplicationrepository.types.status


class GetCloudFormationTemplateResponse(TypedDict):
    application_id: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The application Amazon Resource Name (ARN).</p>"""
    creation_time: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The date and time this resource was created.</p>"""
    expiration_time: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The date and time this template expires. Templates expire 1 hour after creation.</p>"""
    semantic_version: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The semantic version of the application:</p><p> <a href=\"https://semver.org/\">https://semver.org/</a> </p>"""
    status: NotRequired["aws_sdk_serverlessapplicationrepository.types.status.Status"]
    """<p>Status of the template creation workflow.</p><p>Possible values: PREPARING | ACTIVE | EXPIRED </p>"""
    template_id: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The UUID returned by CreateCloudFormationTemplate.</p><p>Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}</p>"""
    template_url: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to the template that can be used to deploy the application using AWS CloudFormation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCloudFormationTemplateResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "expiration_time" in value:
        out["expirationTime"] = value["expiration_time"]
    if "semantic_version" in value:
        out["semanticVersion"] = value["semantic_version"]
    if "status" in value:
        import aws_sdk_serverlessapplicationrepository.types.status

        out["status"] = (
            aws_sdk_serverlessapplicationrepository.types.status.serialize_json(
                value["status"]
            )
        )
    if "template_id" in value:
        out["templateId"] = value["template_id"]
    if "template_url" in value:
        out["templateUrl"] = value["template_url"]
    return out


def deserialize_json(data: dict) -> GetCloudFormationTemplateResponse:
    out: GetCloudFormationTemplateResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
    if "expirationTime" in data:
        out["expiration_time"] = data["expirationTime"]
    if "semanticVersion" in data:
        out["semantic_version"] = data["semanticVersion"]
    if "status" in data:
        import aws_sdk_serverlessapplicationrepository.types.status

        out["status"] = (
            aws_sdk_serverlessapplicationrepository.types.status.deserialize_json(
                data["status"]
            )
        )
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    if "templateUrl" in data:
        out["template_url"] = data["templateUrl"]
    return out
