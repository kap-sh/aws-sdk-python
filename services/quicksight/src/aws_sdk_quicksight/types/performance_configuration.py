"""Generated from Smithy shape ``com.amazonaws.quicksight#PerformanceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.unique_key_list


class PerformanceConfiguration(TypedDict):
    unique_keys: NotRequired["aws_sdk_quicksight.types.unique_key_list.UniqueKeyList"]
    """<p>A <code>UniqueKey</code> configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceConfiguration) -> dict:
    out: dict = {}
    if "unique_keys" in value:
        import aws_sdk_quicksight.types.unique_key_list

        out["UniqueKeys"] = aws_sdk_quicksight.types.unique_key_list.serialize_json(
            value["unique_keys"]
        )
    return out


def deserialize_json(data: dict) -> PerformanceConfiguration:
    out: PerformanceConfiguration = {}  # type: ignore[typeddict-item]
    if "UniqueKeys" in data:
        import aws_sdk_quicksight.types.unique_key_list

        out["unique_keys"] = aws_sdk_quicksight.types.unique_key_list.deserialize_json(
            data["UniqueKeys"]
        )
    return out
