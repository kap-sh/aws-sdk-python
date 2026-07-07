"""Generated from Smithy shape ``com.amazonaws.connect#DataTableDeleteValueIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_lock_version
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.primary_values_set


class DataTableDeleteValueIdentifier(TypedDict, closed=True):
    primary_values: NotRequired[
        "aws_sdk_connect.types.primary_values_set.PrimaryValuesSet"
    ]
    """<p>The identifier's primary values.</p>"""
    attribute_name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The identifier's attribute name.</p>"""
    lock_version: "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The identifier's lock version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableDeleteValueIdentifier) -> dict:
    out: dict = {}
    if "primary_values" in value:
        import aws_sdk_connect.types.primary_values_set

        out["PrimaryValues"] = aws_sdk_connect.types.primary_values_set.serialize_json(
            value["primary_values"]
        )
    out["AttributeName"] = value["attribute_name"]
    import aws_sdk_connect.types.data_table_lock_version

    out["LockVersion"] = aws_sdk_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> DataTableDeleteValueIdentifier:
    out: DataTableDeleteValueIdentifier = {}  # type: ignore[typeddict-item]
    if "PrimaryValues" in data:
        import aws_sdk_connect.types.primary_values_set

        out["primary_values"] = (
            aws_sdk_connect.types.primary_values_set.deserialize_json(
                data["PrimaryValues"]
            )
        )
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError(
            "DataTableDeleteValueIdentifier.attribute_name required"
        )
    if "LockVersion" in data:
        import aws_sdk_connect.types.data_table_lock_version

        out["lock_version"] = (
            aws_sdk_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "DataTableDeleteValueIdentifier.lock_version required"
        )
    return out
