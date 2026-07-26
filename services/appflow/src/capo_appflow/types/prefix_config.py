"""Generated from Smithy shape ``com.amazonaws.appflow#PrefixConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.path_prefix_hierarchy
    import capo_appflow.types.prefix_format
    import capo_appflow.types.prefix_type


class PrefixConfig(TypedDict, closed=True):
    prefix_type: NotRequired["capo_appflow.types.prefix_type.PrefixType"]
    """<p>Determines the format of the prefix, and whether it applies to the file name, file path, or both. </p>"""
    prefix_format: NotRequired["capo_appflow.types.prefix_format.PrefixFormat"]
    """<p>Determines the level of granularity for the date and time that's included in the prefix. </p>"""
    path_prefix_hierarchy: NotRequired[
        "capo_appflow.types.path_prefix_hierarchy.PathPrefixHierarchy"
    ]
    """<p>Specifies whether the destination file path includes either or both of the following elements:</p> <dl> <dt>EXECUTION_ID</dt> <dd> <p>The ID that Amazon AppFlow assigns to the flow run.</p> </dd> <dt>SCHEMA_VERSION</dt> <dd> <p>The version number of your data schema. Amazon AppFlow assigns this version number. The version number increases by one when you change any of the following settings in your flow configuration:</p> <ul> <li> <p>Source-to-destination field mappings</p> </li> <li> <p>Field data types</p> </li> <li> <p>Partition keys</p> </li> </ul> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrefixConfig) -> dict:
    out: dict = {}
    if "prefix_type" in value:
        import capo_appflow.types.prefix_type

        out["prefixType"] = capo_appflow.types.prefix_type.serialize_json(
            value["prefix_type"]
        )
    if "prefix_format" in value:
        import capo_appflow.types.prefix_format

        out["prefixFormat"] = capo_appflow.types.prefix_format.serialize_json(
            value["prefix_format"]
        )
    if "path_prefix_hierarchy" in value:
        import capo_appflow.types.path_prefix_hierarchy

        out["pathPrefixHierarchy"] = (
            capo_appflow.types.path_prefix_hierarchy.serialize_json(
                value["path_prefix_hierarchy"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrefixConfig:
    out: PrefixConfig = {}  # type: ignore[typeddict-item]
    if "prefixType" in data:
        import capo_appflow.types.prefix_type

        out["prefix_type"] = capo_appflow.types.prefix_type.deserialize_json(
            data["prefixType"]
        )
    if "prefixFormat" in data:
        import capo_appflow.types.prefix_format

        out["prefix_format"] = capo_appflow.types.prefix_format.deserialize_json(
            data["prefixFormat"]
        )
    if "pathPrefixHierarchy" in data:
        import capo_appflow.types.path_prefix_hierarchy

        out["path_prefix_hierarchy"] = (
            capo_appflow.types.path_prefix_hierarchy.deserialize_json(
                data["pathPrefixHierarchy"]
            )
        )
    return out
