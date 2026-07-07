"""Generated from Smithy shape ``com.amazonaws.kendra#ContentSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.boolean
    import aws_sdk_kendra.types.data_source_id_list
    import aws_sdk_kendra.types.faq_ids_list


class ContentSourceConfiguration(TypedDict, closed=True):
    data_source_ids: NotRequired[
        "aws_sdk_kendra.types.data_source_id_list.DataSourceIdList"
    ]
    """<p>The identifier of the data sources you want to use for your Amazon Kendra experience.</p>"""
    faq_ids: NotRequired["aws_sdk_kendra.types.faq_ids_list.FaqIdsList"]
    """<p>The identifier of the FAQs that you want to use for your Amazon Kendra experience.</p>"""
    direct_put_content: "aws_sdk_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to use documents you indexed directly using the <code>BatchPutDocument</code> API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentSourceConfiguration) -> dict:
    out: dict = {}
    if "data_source_ids" in value:
        import aws_sdk_kendra.types.data_source_id_list

        out["DataSourceIds"] = (
            aws_sdk_kendra.types.data_source_id_list.serialize_aws_json_1_1(
                value["data_source_ids"]
            )
        )
    if "faq_ids" in value:
        import aws_sdk_kendra.types.faq_ids_list

        out["FaqIds"] = aws_sdk_kendra.types.faq_ids_list.serialize_aws_json_1_1(
            value["faq_ids"]
        )
    out["DirectPutContent"] = value.get("direct_put_content", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ContentSourceConfiguration:
    out: ContentSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "DataSourceIds" in data:
        import aws_sdk_kendra.types.data_source_id_list

        out["data_source_ids"] = (
            aws_sdk_kendra.types.data_source_id_list.deserialize_aws_json_1_1(
                data["DataSourceIds"]
            )
        )
    if "FaqIds" in data:
        import aws_sdk_kendra.types.faq_ids_list

        out["faq_ids"] = aws_sdk_kendra.types.faq_ids_list.deserialize_aws_json_1_1(
            data["FaqIds"]
        )
    if "DirectPutContent" in data:
        out["direct_put_content"] = data["DirectPutContent"]
    else:
        out["direct_put_content"] = False
    return out
