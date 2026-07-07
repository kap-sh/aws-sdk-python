"""Generated from Smithy shape ``com.amazonaws.glue#GetCatalogsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_list
    import aws_sdk_glue.types.token


class GetCatalogsResponse(TypedDict, closed=True):
    catalog_list: "aws_sdk_glue.types.catalog_list.CatalogList"
    """<p>An array of <code>Catalog</code> objects. A list of <code>Catalog</code> objects from the specified parent catalog.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCatalogsResponse) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.catalog_list

    out["CatalogList"] = aws_sdk_glue.types.catalog_list.serialize_aws_json_1_1(
        value["catalog_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCatalogsResponse:
    out: GetCatalogsResponse = {}  # type: ignore[typeddict-item]
    if "CatalogList" in data:
        import aws_sdk_glue.types.catalog_list

        out["catalog_list"] = aws_sdk_glue.types.catalog_list.deserialize_aws_json_1_1(
            data["CatalogList"]
        )
    else:
        raise DeserializationError("GetCatalogsResponse.catalog_list required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
