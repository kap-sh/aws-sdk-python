"""Generated from Smithy shape ``com.amazonaws.glue#TestConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.test_connection_input


class TestConnectionRequest(TypedDict, closed=True):
    connection_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Optional. The name of the connection to test. If only name is provided, the operation will get the connection and use that for testing.</p>"""
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The catalog ID where the connection resides.</p>"""
    test_connection_input: NotRequired[
        "aws_sdk_glue.types.test_connection_input.TestConnectionInput"
    ]
    """<p>A structure that is used to specify testing a connection to a service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestConnectionRequest) -> dict:
    out: dict = {}
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "test_connection_input" in value:
        import aws_sdk_glue.types.test_connection_input

        out["TestConnectionInput"] = (
            aws_sdk_glue.types.test_connection_input.serialize_aws_json_1_1(
                value["test_connection_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestConnectionRequest:
    out: TestConnectionRequest = {}  # type: ignore[typeddict-item]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "TestConnectionInput" in data:
        import aws_sdk_glue.types.test_connection_input

        out["test_connection_input"] = (
            aws_sdk_glue.types.test_connection_input.deserialize_aws_json_1_1(
                data["TestConnectionInput"]
            )
        )
    return out
