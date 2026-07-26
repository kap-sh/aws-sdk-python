"""Generated from Smithy shape ``com.amazonaws.support#Service``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.category_list
    import capo_support.types.service_code
    import capo_support.types.service_name


class Service(TypedDict, closed=True):
    code: NotRequired["capo_support.types.service_code.ServiceCode"]
    """<p>The code for an Amazon Web Services service returned by the <a>DescribeServices</a> response. The <code>name</code> element contains the corresponding friendly name.</p>"""
    name: NotRequired["capo_support.types.service_name.ServiceName"]
    """<p>The friendly name for an Amazon Web Services service. The <code>code</code> element contains the corresponding code.</p>"""
    categories: NotRequired["capo_support.types.category_list.CategoryList"]
    """<p>A list of categories that describe the type of support issue a case describes. Categories consist of a category name and a category code. Category names and codes are passed to Amazon Web Services Support when you call <a>CreateCase</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Service) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "name" in value:
        out["name"] = value["name"]
    if "categories" in value:
        import capo_support.types.category_list

        out["categories"] = capo_support.types.category_list.serialize_aws_json_1_1(
            value["categories"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "name" in data:
        out["name"] = data["name"]
    if "categories" in data:
        import capo_support.types.category_list

        out["categories"] = capo_support.types.category_list.deserialize_aws_json_1_1(
            data["categories"]
        )
    return out
