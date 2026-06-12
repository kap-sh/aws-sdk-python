"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SsmParameterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.account_id
    import aws_sdk_imagebuilder.types.ssm_parameter_data_type
    import aws_sdk_imagebuilder.types.ssm_parameter_name


class SsmParameterConfiguration(TypedDict):
    ami_account_id: NotRequired["aws_sdk_imagebuilder.types.account_id.AccountId"]
    """<p>Specify the account that will own the Parameter in a given Region. During distribution, this account must be specified in distribution settings as a target account for the Region.</p>"""
    parameter_name: "aws_sdk_imagebuilder.types.ssm_parameter_name.SsmParameterName"
    """<p>This is the name of the Parameter in the target Region or account. The image distribution creates the Parameter if it doesn't already exist. Otherwise, it updates the parameter.</p>"""
    data_type: NotRequired[
        "aws_sdk_imagebuilder.types.ssm_parameter_data_type.SsmParameterDataType"
    ]
    """<p>The data type specifies what type of value the Parameter contains. We recommend that you use data type <code>aws:ec2:image</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SsmParameterConfiguration) -> dict:
    out: dict = {}
    if "ami_account_id" in value:
        out["amiAccountId"] = value["ami_account_id"]
    out["parameterName"] = value["parameter_name"]
    if "data_type" in value:
        import aws_sdk_imagebuilder.types.ssm_parameter_data_type

        out["dataType"] = (
            aws_sdk_imagebuilder.types.ssm_parameter_data_type.serialize_json(
                value["data_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> SsmParameterConfiguration:
    out: SsmParameterConfiguration = {}  # type: ignore[typeddict-item]
    if "amiAccountId" in data:
        out["ami_account_id"] = data["amiAccountId"]
    if "parameterName" in data:
        out["parameter_name"] = data["parameterName"]
    else:
        raise DeserializationError("SsmParameterConfiguration.parameter_name required")
    if "dataType" in data:
        import aws_sdk_imagebuilder.types.ssm_parameter_data_type

        out["data_type"] = (
            aws_sdk_imagebuilder.types.ssm_parameter_data_type.deserialize_json(
                data["dataType"]
            )
        )
    return out
