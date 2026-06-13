"""Generated from Smithy shape ``com.amazonaws.securitylake#DeleteDataLakeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.region_list


class DeleteDataLakeRequest(TypedDict):
    regions: "aws_sdk_securitylake.types.region_list.RegionList"
    """<p>The list of Regions where Security Lake is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataLakeRequest) -> dict:
    out: dict = {}
    import aws_sdk_securitylake.types.region_list

    out["regions"] = aws_sdk_securitylake.types.region_list.serialize_json(
        value["regions"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDataLakeRequest:
    out: DeleteDataLakeRequest = {}  # type: ignore[typeddict-item]
    if "regions" in data:
        import aws_sdk_securitylake.types.region_list

        out["regions"] = aws_sdk_securitylake.types.region_list.deserialize_json(
            data["regions"]
        )
    else:
        raise DeserializationError("DeleteDataLakeRequest.regions required")
    return out
