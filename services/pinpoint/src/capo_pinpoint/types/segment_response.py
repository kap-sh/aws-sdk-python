"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.segment_dimensions
    import capo_pinpoint.types.segment_group_list
    import capo_pinpoint.types.segment_import_resource
    import capo_pinpoint.types.segment_type


class SegmentResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the segment is associated with.</p>"""
    arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the segment.</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time when the segment was created.</p>"""
    dimensions: NotRequired["capo_pinpoint.types.segment_dimensions.SegmentDimensions"]
    """<p>The dimension settings for the segment.</p>"""
    id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the segment.</p>"""
    import_definition: NotRequired[
        "capo_pinpoint.types.segment_import_resource.SegmentImportResource"
    ]
    """<p>The settings for the import job that's associated with the segment.</p>"""
    last_modified_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time when the segment was last modified.</p>"""
    name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the segment.</p>"""
    segment_groups: NotRequired[
        "capo_pinpoint.types.segment_group_list.SegmentGroupList"
    ]
    """<p>A list of one or more segment groups that apply to the segment. Each segment group consists of zero or more base segments and the dimensions that are applied to those base segments.</p>"""
    segment_type: NotRequired["capo_pinpoint.types.segment_type.SegmentType"]
    """<p>The segment type. Valid values are:</p> <ul><li><p>DIMENSIONAL - A dynamic segment, which is a segment that uses selection criteria that you specify and is based on endpoint data that's reported by your app. Dynamic segments can change over time.</p></li> <li><p>IMPORT - A static segment, which is a segment that uses selection criteria that you specify and is based on endpoint definitions that you import from a file. Imported segments are static; they don't change over time.</p></li></ul>"""
    tags: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A string-to-string map of key-value pairs that identifies the tags that are associated with the segment. Each tag consists of a required tag key and an associated tag value.</p>"""
    version: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The version number of the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "dimensions" in value:
        import capo_pinpoint.types.segment_dimensions

        out["Dimensions"] = capo_pinpoint.types.segment_dimensions.serialize_json(
            value["dimensions"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "import_definition" in value:
        import capo_pinpoint.types.segment_import_resource

        out["ImportDefinition"] = (
            capo_pinpoint.types.segment_import_resource.serialize_json(
                value["import_definition"]
            )
        )
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "name" in value:
        out["Name"] = value["name"]
    if "segment_groups" in value:
        import capo_pinpoint.types.segment_group_list

        out["SegmentGroups"] = capo_pinpoint.types.segment_group_list.serialize_json(
            value["segment_groups"]
        )
    if "segment_type" in value:
        import capo_pinpoint.types.segment_type

        out["SegmentType"] = capo_pinpoint.types.segment_type.serialize_json(
            value["segment_type"]
        )
    if "tags" in value:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.serialize_json(value["tags"])
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> SegmentResponse:
    out: SegmentResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "Dimensions" in data:
        import capo_pinpoint.types.segment_dimensions

        out["dimensions"] = capo_pinpoint.types.segment_dimensions.deserialize_json(
            data["Dimensions"]
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "ImportDefinition" in data:
        import capo_pinpoint.types.segment_import_resource

        out["import_definition"] = (
            capo_pinpoint.types.segment_import_resource.deserialize_json(
                data["ImportDefinition"]
            )
        )
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SegmentGroups" in data:
        import capo_pinpoint.types.segment_group_list

        out["segment_groups"] = capo_pinpoint.types.segment_group_list.deserialize_json(
            data["SegmentGroups"]
        )
    if "SegmentType" in data:
        import capo_pinpoint.types.segment_type

        out["segment_type"] = capo_pinpoint.types.segment_type.deserialize_json(
            data["SegmentType"]
        )
    if "tags" in data:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.deserialize_json(data["tags"])
    if "Version" in data:
        out["version"] = data["Version"]
    return out
