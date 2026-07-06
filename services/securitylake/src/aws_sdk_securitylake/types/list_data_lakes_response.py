"""Generated from Smithy shape ``com.amazonaws.securitylake#ListDataLakesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_resource_list


class ListDataLakesResponse(TypedDict, closed=True):
    data_lakes: NotRequired[
        "aws_sdk_securitylake.types.data_lake_resource_list.DataLakeResourceList"
    ]
    """<p>Retrieves the Security Lake configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataLakesResponse) -> dict:
    out: dict = {}
    if "data_lakes" in value:
        import aws_sdk_securitylake.types.data_lake_resource_list

        out["dataLakes"] = (
            aws_sdk_securitylake.types.data_lake_resource_list.serialize_json(
                value["data_lakes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDataLakesResponse:
    out: ListDataLakesResponse = {}  # type: ignore[typeddict-item]
    if "dataLakes" in data:
        import aws_sdk_securitylake.types.data_lake_resource_list

        out["data_lakes"] = (
            aws_sdk_securitylake.types.data_lake_resource_list.deserialize_json(
                data["dataLakes"]
            )
        )
    return out
