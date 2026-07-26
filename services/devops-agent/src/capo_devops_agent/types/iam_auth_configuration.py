"""Generated from Smithy shape ``com.amazonaws.devopsagent#IamAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class IamAuthConfiguration(TypedDict, closed=True):
    operator_app_role_arn: "str"
    """<p>The IAM role end users assume to access AIDevOps APIs</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the Operator App IAM auth flow was enabled.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the Operator App IAM auth flow was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamAuthConfiguration) -> dict:
    out: dict = {}
    out["operatorAppRoleArn"] = value["operator_app_role_arn"]
    import capo_devops_agent.types._prelude.timestamp

    out["createdAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_devops_agent.types._prelude.timestamp

        out["updatedAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> IamAuthConfiguration:
    out: IamAuthConfiguration = {}  # type: ignore[typeddict-item]
    if "operatorAppRoleArn" in data:
        out["operator_app_role_arn"] = data["operatorAppRoleArn"]
    else:
        raise DeserializationError(
            "IamAuthConfiguration.operator_app_role_arn required"
        )
    if "createdAt" in data:
        import capo_devops_agent.types._prelude.timestamp

        out["created_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("IamAuthConfiguration.created_at required")
    if "updatedAt" in data:
        import capo_devops_agent.types._prelude.timestamp

        out["updated_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
