"""Generated from Smithy shape ``com.amazonaws.appsync#Integration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.lambda_config
    import capo_appsync.types.string


class Integration(TypedDict, closed=True):
    data_source_name: "capo_appsync.types.string.String"
    """<p>The unique name of the data source that has been configured on the API.</p>"""
    lambda_config: NotRequired["capo_appsync.types.lambda_config.LambdaConfig"]
    """<p>The configuration for a Lambda data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Integration) -> dict:
    out: dict = {}
    out["dataSourceName"] = value["data_source_name"]
    if "lambda_config" in value:
        import capo_appsync.types.lambda_config

        out["lambdaConfig"] = capo_appsync.types.lambda_config.serialize_json(
            value["lambda_config"]
        )
    return out


def deserialize_json(data: dict) -> Integration:
    out: Integration = {}  # type: ignore[typeddict-item]
    if "dataSourceName" in data:
        out["data_source_name"] = data["dataSourceName"]
    else:
        raise DeserializationError("Integration.data_source_name required")
    if "lambdaConfig" in data:
        import capo_appsync.types.lambda_config

        out["lambda_config"] = capo_appsync.types.lambda_config.deserialize_json(
            data["lambdaConfig"]
        )
    return out
