"""Generated from Smithy shape ``com.amazonaws.databrew#PathOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.files_limit
    import aws_sdk_databrew.types.filter_expression
    import aws_sdk_databrew.types.path_parameters_map


class PathOptions(TypedDict, closed=True):
    last_modified_date_condition: NotRequired[
        "aws_sdk_databrew.types.filter_expression.FilterExpression"
    ]
    """<p>If provided, this structure defines a date range for matching Amazon S3 objects based on their LastModifiedDate attribute in Amazon S3.</p>"""
    files_limit: NotRequired["aws_sdk_databrew.types.files_limit.FilesLimit"]
    """<p>If provided, this structure imposes a limit on a number of files that should be selected.</p>"""
    parameters: NotRequired[
        "aws_sdk_databrew.types.path_parameters_map.PathParametersMap"
    ]
    """<p>A structure that maps names of parameters used in the Amazon S3 path of a dataset to their definitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PathOptions) -> dict:
    out: dict = {}
    if "last_modified_date_condition" in value:
        import aws_sdk_databrew.types.filter_expression

        out["LastModifiedDateCondition"] = (
            aws_sdk_databrew.types.filter_expression.serialize_json(
                value["last_modified_date_condition"]
            )
        )
    if "files_limit" in value:
        import aws_sdk_databrew.types.files_limit

        out["FilesLimit"] = aws_sdk_databrew.types.files_limit.serialize_json(
            value["files_limit"]
        )
    if "parameters" in value:
        import aws_sdk_databrew.types.path_parameters_map

        out["Parameters"] = aws_sdk_databrew.types.path_parameters_map.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> PathOptions:
    out: PathOptions = {}  # type: ignore[typeddict-item]
    if "LastModifiedDateCondition" in data:
        import aws_sdk_databrew.types.filter_expression

        out["last_modified_date_condition"] = (
            aws_sdk_databrew.types.filter_expression.deserialize_json(
                data["LastModifiedDateCondition"]
            )
        )
    if "FilesLimit" in data:
        import aws_sdk_databrew.types.files_limit

        out["files_limit"] = aws_sdk_databrew.types.files_limit.deserialize_json(
            data["FilesLimit"]
        )
    if "Parameters" in data:
        import aws_sdk_databrew.types.path_parameters_map

        out["parameters"] = aws_sdk_databrew.types.path_parameters_map.deserialize_json(
            data["Parameters"]
        )
    return out
