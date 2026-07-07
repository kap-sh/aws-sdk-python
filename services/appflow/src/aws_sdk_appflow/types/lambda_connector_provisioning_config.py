"""Generated from Smithy shape ``com.amazonaws.appflow#LambdaConnectorProvisioningConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.arn


class LambdaConnectorProvisioningConfig(TypedDict, closed=True):
    lambda_arn: "aws_sdk_appflow.types.arn.ARN"
    """<p>Lambda ARN of the connector being registered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaConnectorProvisioningConfig) -> dict:
    out: dict = {}
    out["lambdaArn"] = value["lambda_arn"]
    return out


def deserialize_json(data: dict) -> LambdaConnectorProvisioningConfig:
    out: LambdaConnectorProvisioningConfig = {}  # type: ignore[typeddict-item]
    if "lambdaArn" in data:
        out["lambda_arn"] = data["lambdaArn"]
    else:
        raise DeserializationError(
            "LambdaConnectorProvisioningConfig.lambda_arn required"
        )
    return out
