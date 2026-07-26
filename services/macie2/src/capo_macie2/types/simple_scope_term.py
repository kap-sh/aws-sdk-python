"""Generated from Smithy shape ``com.amazonaws.macie2#SimpleScopeTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string
    import capo_macie2.types.job_comparator
    import capo_macie2.types.scope_filter_key


class SimpleScopeTerm(TypedDict, closed=True):
    comparator: NotRequired["capo_macie2.types.job_comparator.JobComparator"]
    """<p>The operator to use in the condition. Valid values for each supported property (key) are:</p> <ul><li><p>OBJECT_EXTENSION - EQ (equals) or NE (not equals)</p></li> <li><p>OBJECT_KEY - STARTS_WITH</p></li> <li><p>OBJECT_LAST_MODIFIED_DATE - EQ (equals), GT (greater than), GTE (greater than or equals), LT (less than), LTE (less than or equals), or NE (not equals)</p></li> <li><p>OBJECT_SIZE - EQ (equals), GT (greater than), GTE (greater than or equals), LT (less than), LTE (less than or equals), or NE (not equals)</p></li></ul>"""
    key: NotRequired["capo_macie2.types.scope_filter_key.ScopeFilterKey"]
    """<p>The object property to use in the condition.</p>"""
    values: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists the values to use in the condition. If the value for the key property is OBJECT_EXTENSION or OBJECT_KEY, this array can specify multiple values and Amazon Macie uses OR logic to join the values. Otherwise, this array can specify only one value.</p> <p>Valid values for each supported property (key) are:</p> <ul><li><p>OBJECT_EXTENSION - A string that represents the file name extension of an object. For example: docx or pdf</p></li> <li><p>OBJECT_KEY - A string that represents the key prefix (folder name or path) of an object. For example: logs or awslogs/eventlogs. This value applies a condition to objects whose keys (names) begin with the specified value.</p></li> <li><p>OBJECT_LAST_MODIFIED_DATE - The date and time (in UTC and extended ISO 8601 format) when an object was created or last changed, whichever is latest. For example: 2023-09-24T14:31:13Z</p></li> <li><p>OBJECT_SIZE - An integer that represents the storage size (in bytes) of an object.</p></li></ul> <p>Macie doesn't support use of wildcard characters in these values. Also, string values are case sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimpleScopeTerm) -> dict:
    out: dict = {}
    if "comparator" in value:
        import capo_macie2.types.job_comparator

        out["comparator"] = capo_macie2.types.job_comparator.serialize_json(
            value["comparator"]
        )
    if "key" in value:
        import capo_macie2.types.scope_filter_key

        out["key"] = capo_macie2.types.scope_filter_key.serialize_json(value["key"])
    if "values" in value:
        import capo_macie2.types.__list_of__string

        out["values"] = capo_macie2.types.__list_of__string.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> SimpleScopeTerm:
    out: SimpleScopeTerm = {}  # type: ignore[typeddict-item]
    if "comparator" in data:
        import capo_macie2.types.job_comparator

        out["comparator"] = capo_macie2.types.job_comparator.deserialize_json(
            data["comparator"]
        )
    if "key" in data:
        import capo_macie2.types.scope_filter_key

        out["key"] = capo_macie2.types.scope_filter_key.deserialize_json(data["key"])
    if "values" in data:
        import capo_macie2.types.__list_of__string

        out["values"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["values"]
        )
    return out
