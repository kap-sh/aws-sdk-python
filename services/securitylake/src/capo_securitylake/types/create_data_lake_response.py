"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateDataLakeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.data_lake_resource_list


class CreateDataLakeResponse(TypedDict, closed=True):
    data_lakes: NotRequired[
        "capo_securitylake.types.data_lake_resource_list.DataLakeResourceList"
    ]
    """<p>The created Security Lake configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataLakeResponse) -> dict:
    out: dict = {}
    if "data_lakes" in value:
        import capo_securitylake.types.data_lake_resource_list

        out["dataLakes"] = (
            capo_securitylake.types.data_lake_resource_list.serialize_json(
                value["data_lakes"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDataLakeResponse:
    out: CreateDataLakeResponse = {}  # type: ignore[typeddict-item]
    if "dataLakes" in data:
        import capo_securitylake.types.data_lake_resource_list

        out["data_lakes"] = (
            capo_securitylake.types.data_lake_resource_list.deserialize_json(
                data["dataLakes"]
            )
        )
    return out
