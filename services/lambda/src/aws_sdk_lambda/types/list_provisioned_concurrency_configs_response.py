"""Generated from Smithy shape ``com.amazonaws.lambda#ListProvisionedConcurrencyConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.provisioned_concurrency_config_list
    import aws_sdk_lambda.types.string


class ListProvisionedConcurrencyConfigsResponse(TypedDict):
    provisioned_concurrency_configs: NotRequired[
        "aws_sdk_lambda.types.provisioned_concurrency_config_list.ProvisionedConcurrencyConfigList"
    ]
    """<p>A list of provisioned concurrency configurations.</p>"""
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProvisionedConcurrencyConfigsResponse) -> dict:
    out: dict = {}
    if "provisioned_concurrency_configs" in value:
        import aws_sdk_lambda.types.provisioned_concurrency_config_list

        out["ProvisionedConcurrencyConfigs"] = (
            aws_sdk_lambda.types.provisioned_concurrency_config_list.serialize_json(
                value["provisioned_concurrency_configs"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListProvisionedConcurrencyConfigsResponse:
    out: ListProvisionedConcurrencyConfigsResponse = {}  # type: ignore[typeddict-item]
    if "ProvisionedConcurrencyConfigs" in data:
        import aws_sdk_lambda.types.provisioned_concurrency_config_list

        out["provisioned_concurrency_configs"] = (
            aws_sdk_lambda.types.provisioned_concurrency_config_list.deserialize_json(
                data["ProvisionedConcurrencyConfigs"]
            )
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
