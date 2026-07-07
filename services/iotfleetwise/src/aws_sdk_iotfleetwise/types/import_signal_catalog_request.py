"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ImportSignalCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.formatted_vss
    import aws_sdk_iotfleetwise.types.resource_name
    import aws_sdk_iotfleetwise.types.tag_list


class ImportSignalCatalogRequest(TypedDict, closed=True):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p>The name of the signal catalog to import.</p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p> A brief description of the signal catalog. </p>"""
    vss: NotRequired["aws_sdk_iotfleetwise.types.formatted_vss.FormattedVss"]
    """<p>The contents of the Vehicle Signal Specification (VSS) configuration. VSS is a precise language used to describe and model signals in vehicle networks.</p>"""
    tags: NotRequired["aws_sdk_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the signal catalog.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportSignalCatalogRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "vss" in value:
        import aws_sdk_iotfleetwise.types.formatted_vss

        out["vss"] = aws_sdk_iotfleetwise.types.formatted_vss.serialize_aws_json_1_0(
            value["vss"]
        )
    if "tags" in value:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportSignalCatalogRequest:
    out: ImportSignalCatalogRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "vss" in data:
        import aws_sdk_iotfleetwise.types.formatted_vss

        out["vss"] = aws_sdk_iotfleetwise.types.formatted_vss.deserialize_aws_json_1_0(
            data["vss"]
        )
    if "tags" in data:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
