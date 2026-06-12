"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaLinuxProcessParams``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.lambda_container_params
    import aws_sdk_greengrassv2.types.lambda_isolation_mode


class LambdaLinuxProcessParams(TypedDict):
    isolation_mode: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_isolation_mode.LambdaIsolationMode"
    ]
    """<p>The isolation mode for the process that contains the Lambda function. The process can run in an isolated runtime environment inside the IoT Greengrass container, or as a regular process outside any container.</p> <p>Default: <code>GreengrassContainer</code> </p>"""
    container_params: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_container_params.LambdaContainerParams"
    ]
    """<p>The parameters for the container in which the Lambda function runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaLinuxProcessParams) -> dict:
    out: dict = {}
    if "isolation_mode" in value:
        import aws_sdk_greengrassv2.types.lambda_isolation_mode

        out["isolationMode"] = (
            aws_sdk_greengrassv2.types.lambda_isolation_mode.serialize_json(
                value["isolation_mode"]
            )
        )
    if "container_params" in value:
        import aws_sdk_greengrassv2.types.lambda_container_params

        out["containerParams"] = (
            aws_sdk_greengrassv2.types.lambda_container_params.serialize_json(
                value["container_params"]
            )
        )
    return out


def deserialize_json(data: dict) -> LambdaLinuxProcessParams:
    out: LambdaLinuxProcessParams = {}  # type: ignore[typeddict-item]
    if "isolationMode" in data:
        import aws_sdk_greengrassv2.types.lambda_isolation_mode

        out["isolation_mode"] = (
            aws_sdk_greengrassv2.types.lambda_isolation_mode.deserialize_json(
                data["isolationMode"]
            )
        )
    if "containerParams" in data:
        import aws_sdk_greengrassv2.types.lambda_container_params

        out["container_params"] = (
            aws_sdk_greengrassv2.types.lambda_container_params.deserialize_json(
                data["containerParams"]
            )
        )
    return out
