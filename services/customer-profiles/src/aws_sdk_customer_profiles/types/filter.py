"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.group_list
    import aws_sdk_customer_profiles.types.include


class Filter(TypedDict, closed=True):
    include: "aws_sdk_customer_profiles.types.include.Include"
    """<p>Define whether to include or exclude objects for Calculated Attributed calculation that fit the filter groups criteria.</p>"""
    groups: "aws_sdk_customer_profiles.types.group_list.GroupList"
    """<p>Holds the list of Filter groups within the Filter definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.include

    out["Include"] = aws_sdk_customer_profiles.types.include.serialize_json(
        value["include"]
    )
    import aws_sdk_customer_profiles.types.group_list

    out["Groups"] = aws_sdk_customer_profiles.types.group_list.serialize_json(
        value["groups"]
    )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Include" in data:
        import aws_sdk_customer_profiles.types.include

        out["include"] = aws_sdk_customer_profiles.types.include.deserialize_json(
            data["Include"]
        )
    else:
        raise DeserializationError("Filter.include required")
    if "Groups" in data:
        import aws_sdk_customer_profiles.types.group_list

        out["groups"] = aws_sdk_customer_profiles.types.group_list.deserialize_json(
            data["Groups"]
        )
    else:
        raise DeserializationError("Filter.groups required")
    return out
