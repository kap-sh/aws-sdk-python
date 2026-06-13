"""Generated from Smithy shape ``com.amazonaws.ssmincidents#FindingDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.cloud_formation_stack_update
    import aws_sdk_ssm_incidents.types.code_deploy_deployment


class _FindingDetails_codeDeployDeployment(TypedDict):
    codeDeployDeployment: (
        "aws_sdk_ssm_incidents.types.code_deploy_deployment.CodeDeployDeployment"
    )


class _FindingDetails_cloudFormationStackUpdate(TypedDict):
    cloudFormationStackUpdate: "aws_sdk_ssm_incidents.types.cloud_formation_stack_update.CloudFormationStackUpdate"


FindingDetails: TypeAlias = (
    _FindingDetails_codeDeployDeployment | _FindingDetails_cloudFormationStackUpdate
)


# --- restJson1 ser/de ---
def serialize_json(value: FindingDetails) -> dict:
    if "codeDeployDeployment" in value:
        import aws_sdk_ssm_incidents.types.code_deploy_deployment

        return {
            "codeDeployDeployment": aws_sdk_ssm_incidents.types.code_deploy_deployment.serialize_json(
                value["codeDeployDeployment"]
            )
        }
    elif "cloudFormationStackUpdate" in value:
        import aws_sdk_ssm_incidents.types.cloud_formation_stack_update

        return {
            "cloudFormationStackUpdate": aws_sdk_ssm_incidents.types.cloud_formation_stack_update.serialize_json(
                value["cloudFormationStackUpdate"]
            )
        }
    else:
        raise SerializationError("FindingDetails: no variant present")


def deserialize_json(data: dict) -> FindingDetails:
    if "codeDeployDeployment" in data:
        import aws_sdk_ssm_incidents.types.code_deploy_deployment

        return {
            "codeDeployDeployment": aws_sdk_ssm_incidents.types.code_deploy_deployment.deserialize_json(
                data["codeDeployDeployment"]
            )
        }
    elif "cloudFormationStackUpdate" in data:
        import aws_sdk_ssm_incidents.types.cloud_formation_stack_update

        return {
            "cloudFormationStackUpdate": aws_sdk_ssm_incidents.types.cloud_formation_stack_update.deserialize_json(
                data["cloudFormationStackUpdate"]
            )
        }
    else:
        raise DeserializationError("FindingDetails: no recognized variant key")
