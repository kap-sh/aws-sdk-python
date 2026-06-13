"""Generated from Smithy shape ``com.amazonaws.devopsagent#IdcAuthConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class IdcAuthConfiguration(TypedDict):
    operator_app_role_arn: "str"
    """<p>The IAM role end users assume to access AIDevOps APIs</p>"""
    idc_instance_arn: "str"
    """<p>The IdC instance Arn used to create an IdC auth application</p>"""
    idc_application_arn: NotRequired["str"]
    """<p>The IdC application Arn created for IdC auth</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the Operator App IdC auth flow was enabled.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the Operator App IdC auth flow was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdcAuthConfiguration) -> dict:
    out: dict = {}
    out["operatorAppRoleArn"] = value["operator_app_role_arn"]
    out["idcInstanceArn"] = value["idc_instance_arn"]
    if "idc_application_arn" in value:
        out["idcApplicationArn"] = value["idc_application_arn"]
    import aws_sdk_devops_agent.types._prelude.timestamp

    out["createdAt"] = aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> IdcAuthConfiguration:
    out: IdcAuthConfiguration = {}  # type: ignore[typeddict-item]
    if "operatorAppRoleArn" in data:
        out["operator_app_role_arn"] = data["operatorAppRoleArn"]
    else:
        raise DeserializationError(
            "IdcAuthConfiguration.operator_app_role_arn required"
        )
    if "idcInstanceArn" in data:
        out["idc_instance_arn"] = data["idcInstanceArn"]
    else:
        raise DeserializationError("IdcAuthConfiguration.idc_instance_arn required")
    if "idcApplicationArn" in data:
        out["idc_application_arn"] = data["idcApplicationArn"]
    if "createdAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("IdcAuthConfiguration.created_at required")
    if "updatedAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
