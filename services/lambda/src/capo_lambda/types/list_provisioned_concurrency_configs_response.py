"""Generated from Smithy shape ``com.amazonaws.lambda#ListProvisionedConcurrencyConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.provisioned_concurrency_config_list
    import capo_lambda.types.string


class ListProvisionedConcurrencyConfigsResponse(TypedDict, closed=True):
    provisioned_concurrency_configs: NotRequired[
        "capo_lambda.types.provisioned_concurrency_config_list.ProvisionedConcurrencyConfigList"
    ]
    """<p>A list of provisioned concurrency configurations.</p>"""
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProvisionedConcurrencyConfigsResponse) -> dict:
    out: dict = {}
    if "provisioned_concurrency_configs" in value:
        import capo_lambda.types.provisioned_concurrency_config_list

        out["ProvisionedConcurrencyConfigs"] = (
            capo_lambda.types.provisioned_concurrency_config_list.serialize_json(
                value["provisioned_concurrency_configs"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListProvisionedConcurrencyConfigsResponse:
    out: ListProvisionedConcurrencyConfigsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedConcurrencyConfigs") is not None:
        import capo_lambda.types.provisioned_concurrency_config_list

        out["provisioned_concurrency_configs"] = (
            capo_lambda.types.provisioned_concurrency_config_list.deserialize_json(
                data["ProvisionedConcurrencyConfigs"]
            )
        )
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
