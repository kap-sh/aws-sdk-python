"""Generated from Smithy shape ``com.amazonaws.ssm#Activation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.activation_description
    import aws_sdk_ssm.types.activation_id
    import aws_sdk_ssm.types.boolean
    import aws_sdk_ssm.types.created_date
    import aws_sdk_ssm.types.default_instance_name
    import aws_sdk_ssm.types.expiration_date
    import aws_sdk_ssm.types.iam_role
    import aws_sdk_ssm.types.registration_limit
    import aws_sdk_ssm.types.registrations_count
    import aws_sdk_ssm.types.tag_list


class Activation(TypedDict):
    activation_id: NotRequired["aws_sdk_ssm.types.activation_id.ActivationId"]
    """<p>The ID created by Systems Manager when you submitted the activation.</p>"""
    description: NotRequired[
        "aws_sdk_ssm.types.activation_description.ActivationDescription"
    ]
    """<p>A user defined description of the activation.</p>"""
    default_instance_name: NotRequired[
        "aws_sdk_ssm.types.default_instance_name.DefaultInstanceName"
    ]
    """<p>A name for the managed node when it is created.</p>"""
    iam_role: NotRequired["aws_sdk_ssm.types.iam_role.IamRole"]
    """<p>The Identity and Access Management (IAM) role to assign to the managed node.</p>"""
    registration_limit: NotRequired[
        "aws_sdk_ssm.types.registration_limit.RegistrationLimit"
    ]
    """<p>The maximum number of managed nodes that can be registered using this activation.</p>"""
    registrations_count: NotRequired[
        "aws_sdk_ssm.types.registrations_count.RegistrationsCount"
    ]
    """<p>The number of managed nodes already registered with this activation.</p>"""
    expiration_date: NotRequired["aws_sdk_ssm.types.expiration_date.ExpirationDate"]
    """<p>The date when this activation can no longer be used to register managed nodes.</p>"""
    expired: "aws_sdk_ssm.types.boolean.Boolean"
    """<p>Whether or not the activation is expired.</p>"""
    created_date: NotRequired["aws_sdk_ssm.types.created_date.CreatedDate"]
    """<p>The date the activation was created.</p>"""
    tags: NotRequired["aws_sdk_ssm.types.tag_list.TagList"]
    """<p>Tags assigned to the activation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Activation) -> dict:
    out: dict = {}
    if "activation_id" in value:
        out["ActivationId"] = value["activation_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "default_instance_name" in value:
        out["DefaultInstanceName"] = value["default_instance_name"]
    if "iam_role" in value:
        out["IamRole"] = value["iam_role"]
    if "registration_limit" in value:
        out["RegistrationLimit"] = value["registration_limit"]
    if "registrations_count" in value:
        out["RegistrationsCount"] = value["registrations_count"]
    if "expiration_date" in value:
        import aws_sdk_ssm.types.expiration_date

        out["ExpirationDate"] = (
            aws_sdk_ssm.types.expiration_date.serialize_aws_json_1_1(
                value["expiration_date"]
            )
        )
    out["Expired"] = value.get("expired", False)
    if "created_date" in value:
        import aws_sdk_ssm.types.created_date

        out["CreatedDate"] = aws_sdk_ssm.types.created_date.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "tags" in value:
        import aws_sdk_ssm.types.tag_list

        out["Tags"] = aws_sdk_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Activation:
    out: Activation = {}  # type: ignore[typeddict-item]
    if "ActivationId" in data:
        out["activation_id"] = data["ActivationId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DefaultInstanceName" in data:
        out["default_instance_name"] = data["DefaultInstanceName"]
    if "IamRole" in data:
        out["iam_role"] = data["IamRole"]
    if "RegistrationLimit" in data:
        out["registration_limit"] = data["RegistrationLimit"]
    if "RegistrationsCount" in data:
        out["registrations_count"] = data["RegistrationsCount"]
    if "ExpirationDate" in data:
        import aws_sdk_ssm.types.expiration_date

        out["expiration_date"] = (
            aws_sdk_ssm.types.expiration_date.deserialize_aws_json_1_1(
                data["ExpirationDate"]
            )
        )
    if "Expired" in data:
        out["expired"] = data["Expired"]
    else:
        out["expired"] = False
    if "CreatedDate" in data:
        import aws_sdk_ssm.types.created_date

        out["created_date"] = aws_sdk_ssm.types.created_date.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if "Tags" in data:
        import aws_sdk_ssm.types.tag_list

        out["tags"] = aws_sdk_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
