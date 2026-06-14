"""Generated from Smithy shape ``com.amazonaws.lambda#Environment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.environment_variables


class Environment(TypedDict):
    variables: NotRequired[
        "aws_sdk_lambda.types.environment_variables.EnvironmentVariables"
    ]
    r"""<p>Environment variable key-value pairs. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html\">Using Lambda environment variables</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Environment) -> dict:
    out: dict = {}
    if "variables" in value:
        import aws_sdk_lambda.types.environment_variables

        out["Variables"] = aws_sdk_lambda.types.environment_variables.serialize_json(
            value["variables"]
        )
    return out


def deserialize_json(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if "Variables" in data:
        import aws_sdk_lambda.types.environment_variables

        out["variables"] = aws_sdk_lambda.types.environment_variables.deserialize_json(
            data["Variables"]
        )
    return out
