"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DataEncryptionMetadata``."""

from typing import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError


class DataEncryptionMetadata(TypedDict):
    allow_cleartext: "bool"
    """<p>Indicates whether encrypted tables can contain cleartext data (<code>TRUE</code>) or are to cryptographically process every column (<code>FALSE</code>).</p>"""
    allow_duplicates: "bool"
    """<p>Indicates whether Fingerprint columns can contain duplicate entries (<code>TRUE</code>) or are to contain only non-repeated values (<code>FALSE</code>).</p>"""
    allow_joins_on_columns_with_different_names: "bool"
    """<p>Indicates whether Fingerprint columns can be joined on any other Fingerprint column with a different name (<code>TRUE</code>) or can only be joined on Fingerprint columns of the same name (<code>FALSE</code>).</p>"""
    preserve_nulls: "bool"
    """<p>Indicates whether NULL values are to be copied as NULL to encrypted tables (<code>TRUE</code>) or cryptographically processed (<code>FALSE</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataEncryptionMetadata) -> dict:
    out: dict = {}
    out["allowCleartext"] = value["allow_cleartext"]
    out["allowDuplicates"] = value["allow_duplicates"]
    out["allowJoinsOnColumnsWithDifferentNames"] = value[
        "allow_joins_on_columns_with_different_names"
    ]
    out["preserveNulls"] = value["preserve_nulls"]
    return out


def deserialize_json(data: dict) -> DataEncryptionMetadata:
    out: DataEncryptionMetadata = {}  # type: ignore[typeddict-item]
    if "allowCleartext" in data:
        out["allow_cleartext"] = data["allowCleartext"]
    else:
        raise DeserializationError("DataEncryptionMetadata.allow_cleartext required")
    if "allowDuplicates" in data:
        out["allow_duplicates"] = data["allowDuplicates"]
    else:
        raise DeserializationError("DataEncryptionMetadata.allow_duplicates required")
    if "allowJoinsOnColumnsWithDifferentNames" in data:
        out["allow_joins_on_columns_with_different_names"] = data[
            "allowJoinsOnColumnsWithDifferentNames"
        ]
    else:
        raise DeserializationError(
            "DataEncryptionMetadata.allow_joins_on_columns_with_different_names required"
        )
    if "preserveNulls" in data:
        out["preserve_nulls"] = data["preserveNulls"]
    else:
        raise DeserializationError("DataEncryptionMetadata.preserve_nulls required")
    return out
