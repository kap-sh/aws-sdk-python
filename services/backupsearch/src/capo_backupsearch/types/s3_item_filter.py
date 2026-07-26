"""Generated from Smithy shape ``com.amazonaws.backupsearch#S3ItemFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backupsearch.types.long_condition_list
    import capo_backupsearch.types.string_condition_list
    import capo_backupsearch.types.time_condition_list


class S3ItemFilter(TypedDict, closed=True):
    object_keys: NotRequired[
        "capo_backupsearch.types.string_condition_list.StringConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one value is included, the results will return only items that match the value.</p> <p>If more than one value is included, the results will return all items that match any of the values.</p>"""
    sizes: NotRequired["capo_backupsearch.types.long_condition_list.LongConditionList"]
    """<p>You can include 1 to 10 values.</p> <p>If one value is included, the results will return only items that match the value.</p> <p>If more than one value is included, the results will return all items that match any of the values.</p>"""
    creation_times: NotRequired[
        "capo_backupsearch.types.time_condition_list.TimeConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one value is included, the results will return only items that match the value.</p> <p>If more than one value is included, the results will return all items that match any of the values.</p>"""
    version_ids: NotRequired[
        "capo_backupsearch.types.string_condition_list.StringConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one value is included, the results will return only items that match the value.</p> <p>If more than one value is included, the results will return all items that match any of the values.</p>"""
    e_tags: NotRequired[
        "capo_backupsearch.types.string_condition_list.StringConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one value is included, the results will return only items that match the value.</p> <p>If more than one value is included, the results will return all items that match any of the values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ItemFilter) -> dict:
    out: dict = {}
    if "object_keys" in value:
        import capo_backupsearch.types.string_condition_list

        out["ObjectKeys"] = (
            capo_backupsearch.types.string_condition_list.serialize_json(
                value["object_keys"]
            )
        )
    if "sizes" in value:
        import capo_backupsearch.types.long_condition_list

        out["Sizes"] = capo_backupsearch.types.long_condition_list.serialize_json(
            value["sizes"]
        )
    if "creation_times" in value:
        import capo_backupsearch.types.time_condition_list

        out["CreationTimes"] = (
            capo_backupsearch.types.time_condition_list.serialize_json(
                value["creation_times"]
            )
        )
    if "version_ids" in value:
        import capo_backupsearch.types.string_condition_list

        out["VersionIds"] = (
            capo_backupsearch.types.string_condition_list.serialize_json(
                value["version_ids"]
            )
        )
    if "e_tags" in value:
        import capo_backupsearch.types.string_condition_list

        out["ETags"] = capo_backupsearch.types.string_condition_list.serialize_json(
            value["e_tags"]
        )
    return out


def deserialize_json(data: dict) -> S3ItemFilter:
    out: S3ItemFilter = {}  # type: ignore[typeddict-item]
    if "ObjectKeys" in data:
        import capo_backupsearch.types.string_condition_list

        out["object_keys"] = (
            capo_backupsearch.types.string_condition_list.deserialize_json(
                data["ObjectKeys"]
            )
        )
    if "Sizes" in data:
        import capo_backupsearch.types.long_condition_list

        out["sizes"] = capo_backupsearch.types.long_condition_list.deserialize_json(
            data["Sizes"]
        )
    if "CreationTimes" in data:
        import capo_backupsearch.types.time_condition_list

        out["creation_times"] = (
            capo_backupsearch.types.time_condition_list.deserialize_json(
                data["CreationTimes"]
            )
        )
    if "VersionIds" in data:
        import capo_backupsearch.types.string_condition_list

        out["version_ids"] = (
            capo_backupsearch.types.string_condition_list.deserialize_json(
                data["VersionIds"]
            )
        )
    if "ETags" in data:
        import capo_backupsearch.types.string_condition_list

        out["e_tags"] = capo_backupsearch.types.string_condition_list.deserialize_json(
            data["ETags"]
        )
    return out
