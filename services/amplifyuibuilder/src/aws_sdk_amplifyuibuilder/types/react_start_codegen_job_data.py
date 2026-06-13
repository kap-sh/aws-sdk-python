"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ReactStartCodegenJobData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.api_configuration
    import aws_sdk_amplifyuibuilder.types.js_module
    import aws_sdk_amplifyuibuilder.types.js_script
    import aws_sdk_amplifyuibuilder.types.js_target
    import aws_sdk_amplifyuibuilder.types.react_codegen_dependencies


class ReactStartCodegenJobData(TypedDict):
    module: NotRequired["aws_sdk_amplifyuibuilder.types.js_module.JSModule"]
    """<p>The JavaScript module type.</p>"""
    target: NotRequired["aws_sdk_amplifyuibuilder.types.js_target.JSTarget"]
    """<p>The ECMAScript specification to use.</p>"""
    script: NotRequired["aws_sdk_amplifyuibuilder.types.js_script.JSScript"]
    """<p>The file type to use for a JavaScript project.</p>"""
    render_type_declarations: "bool"
    """<p>Specifies whether the code generation job should render type declaration files.</p>"""
    inline_source_map: "bool"
    """<p>Specifies whether the code generation job should render inline source maps.</p>"""
    api_configuration: NotRequired[
        "aws_sdk_amplifyuibuilder.types.api_configuration.ApiConfiguration"
    ]
    """<p>The API configuration for the code generation job.</p>"""
    dependencies: NotRequired[
        "aws_sdk_amplifyuibuilder.types.react_codegen_dependencies.ReactCodegenDependencies"
    ]
    """<p>Lists the dependency packages that may be required for the project code to run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReactStartCodegenJobData) -> dict:
    out: dict = {}
    if "module" in value:
        import aws_sdk_amplifyuibuilder.types.js_module

        out["module"] = aws_sdk_amplifyuibuilder.types.js_module.serialize_json(
            value["module"]
        )
    if "target" in value:
        import aws_sdk_amplifyuibuilder.types.js_target

        out["target"] = aws_sdk_amplifyuibuilder.types.js_target.serialize_json(
            value["target"]
        )
    if "script" in value:
        import aws_sdk_amplifyuibuilder.types.js_script

        out["script"] = aws_sdk_amplifyuibuilder.types.js_script.serialize_json(
            value["script"]
        )
    out["renderTypeDeclarations"] = value.get("render_type_declarations", False)
    out["inlineSourceMap"] = value.get("inline_source_map", False)
    if "api_configuration" in value:
        import aws_sdk_amplifyuibuilder.types.api_configuration

        out["apiConfiguration"] = (
            aws_sdk_amplifyuibuilder.types.api_configuration.serialize_json(
                value["api_configuration"]
            )
        )
    if "dependencies" in value:
        import aws_sdk_amplifyuibuilder.types.react_codegen_dependencies

        out["dependencies"] = (
            aws_sdk_amplifyuibuilder.types.react_codegen_dependencies.serialize_json(
                value["dependencies"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReactStartCodegenJobData:
    out: ReactStartCodegenJobData = {}  # type: ignore[typeddict-item]
    if "module" in data:
        import aws_sdk_amplifyuibuilder.types.js_module

        out["module"] = aws_sdk_amplifyuibuilder.types.js_module.deserialize_json(
            data["module"]
        )
    if "target" in data:
        import aws_sdk_amplifyuibuilder.types.js_target

        out["target"] = aws_sdk_amplifyuibuilder.types.js_target.deserialize_json(
            data["target"]
        )
    if "script" in data:
        import aws_sdk_amplifyuibuilder.types.js_script

        out["script"] = aws_sdk_amplifyuibuilder.types.js_script.deserialize_json(
            data["script"]
        )
    if "renderTypeDeclarations" in data:
        out["render_type_declarations"] = data["renderTypeDeclarations"]
    else:
        out["render_type_declarations"] = False
    if "inlineSourceMap" in data:
        out["inline_source_map"] = data["inlineSourceMap"]
    else:
        out["inline_source_map"] = False
    if "apiConfiguration" in data:
        import aws_sdk_amplifyuibuilder.types.api_configuration

        out["api_configuration"] = (
            aws_sdk_amplifyuibuilder.types.api_configuration.deserialize_json(
                data["apiConfiguration"]
            )
        )
    if "dependencies" in data:
        import aws_sdk_amplifyuibuilder.types.react_codegen_dependencies

        out["dependencies"] = (
            aws_sdk_amplifyuibuilder.types.react_codegen_dependencies.deserialize_json(
                data["dependencies"]
            )
        )
    return out
