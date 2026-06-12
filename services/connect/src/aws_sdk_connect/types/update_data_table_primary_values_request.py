"""Generated from Smithy shape ``com.amazonaws.connect#UpdateDataTablePrimaryValuesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.data_table_lock_version
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.primary_values_set


class UpdateDataTablePrimaryValuesRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias. If the version is provided as part of the identifier or ARN, the version must be one of the two available system managed aliases, $SAVED or $LATEST.</p>"""
    primary_values: "aws_sdk_connect.types.primary_values_set.PrimaryValuesSet"
    """<p>The current primary values for the record. Required and must include values for all primary attributes. Fails if the table has primary attributes and some primary values are omitted.</p>"""
    new_primary_values: "aws_sdk_connect.types.primary_values_set.PrimaryValuesSet"
    """<p>The new primary values for the record. Required and must include values for all primary attributes. The combination must be unique within the table.</p>"""
    lock_version: "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The lock version information required for optimistic locking to prevent concurrent modifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataTablePrimaryValuesRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.primary_values_set

    out["PrimaryValues"] = aws_sdk_connect.types.primary_values_set.serialize_json(
        value["primary_values"]
    )
    import aws_sdk_connect.types.primary_values_set

    out["NewPrimaryValues"] = aws_sdk_connect.types.primary_values_set.serialize_json(
        value["new_primary_values"]
    )
    import aws_sdk_connect.types.data_table_lock_version

    out["LockVersion"] = aws_sdk_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataTablePrimaryValuesRequest:
    out: UpdateDataTablePrimaryValuesRequest = {}  # type: ignore[typeddict-item]
    if "PrimaryValues" in data:
        import aws_sdk_connect.types.primary_values_set

        out["primary_values"] = (
            aws_sdk_connect.types.primary_values_set.deserialize_json(
                data["PrimaryValues"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataTablePrimaryValuesRequest.primary_values required"
        )
    if "NewPrimaryValues" in data:
        import aws_sdk_connect.types.primary_values_set

        out["new_primary_values"] = (
            aws_sdk_connect.types.primary_values_set.deserialize_json(
                data["NewPrimaryValues"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataTablePrimaryValuesRequest.new_primary_values required"
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
            "UpdateDataTablePrimaryValuesRequest.lock_version required"
        )
    return out
