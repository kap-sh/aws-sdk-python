"""Generated from Smithy shape ``com.amazonaws.appflow#SAPODataPaginationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.sapo_data_max_page_size


class SAPODataPaginationConfig(TypedDict, closed=True):
    max_page_size: "aws_sdk_appflow.types.sapo_data_max_page_size.SAPODataMaxPageSize"
    """<p>The maximum number of records that Amazon AppFlow receives in each page of the response from your SAP application. For transfers of OData records, the maximum page size is 3,000. For transfers of data that comes from an ODP provider, the maximum page size is 10,000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAPODataPaginationConfig) -> dict:
    out: dict = {}
    out["maxPageSize"] = value["max_page_size"]
    return out


def deserialize_json(data: dict) -> SAPODataPaginationConfig:
    out: SAPODataPaginationConfig = {}  # type: ignore[typeddict-item]
    if "maxPageSize" in data:
        out["max_page_size"] = data["maxPageSize"]
    else:
        raise DeserializationError("SAPODataPaginationConfig.max_page_size required")
    return out
